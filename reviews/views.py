from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from profiles.models import Profile
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, category, product_id):
    """
    Allows authenticated users to add a product review
    """
    if request.user:
        product = get_object_or_404(Product, pk=product_id)
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product = product
                review.author = profile
                review_form.save()

                messages.success(request, "Review added successfully.")
                return redirect('product_item', category=category,
                                product_id=product_id)
            else:
                messages.error(request,
                               "There was an issue with the form. Please try again.")  # noqa: E501
        else:
            review_form = ReviewForm()
    else:
        messages.error(request, "Only logged-in users can post reviews!")
        return redirect('product_item', category=category,
                        product_id=product_id)

    context = {
        "review_form": review_form,
        "category": category,
        "product_id": product_id
    }
    return render(request, "reviews/add_review.html", context=context)


@login_required
def edit_review(request, category, product_id, review_id):
    """
    Allows the user to edit a review, but only if it belongs
    to them
    """
    if request.user:
        product = get_object_or_404(Product, pk=product_id)
        review = get_object_or_404(Review, pk=review_id)
        profile = get_object_or_404(Profile, user=request.user)

        if request.method == "POST":
            if review.author == profile:
                review_form = ReviewForm(request.POST, instance=review)
                if review_form.is_valid():
                    review = review_form.save(commit=False)
                    review.product = product
                    review.author = profile
                    review_form.save()

                    messages.success(request, "Review edited successfully.")
                    return redirect('product_item', category=category,
                                    product_id=product_id)
                else:
                    messages.error(request,
                                   "There was an issue with the form. Please try again.")  # noqa: E501
            else:
                messages.error(request, "You can only edit your own reviews!")
                return redirect('product_item', category=category,
                                product_id=product_id)
        else:
            review_form = ReviewForm(instance=review)
    else:
        messages.error(request, "Only logged-in users can edit reviews!")
        return redirect('home')

    context = {
        "review_form": review_form,
        "category": category,
        "product_id": product_id,
        "review_id": review_id
    }
    return render(request, "reviews/edit_review.html", context=context)


@login_required
def delete_review(request, category, product_id, review_id):
    """
    Allows the user to delete a review, but only if it belongs
    to them. An admin can also delete reviews.
    """
    if request.user:
        product = get_object_or_404(Product, pk=product_id)
        review = get_object_or_404(Review, pk=review_id)
        profile = get_object_or_404(Profile, user=request.user)

        # Only the review author or an admin can delete the review
        if review.author == profile or request.user.is_superuser:
            messages.success(request, "Review deleted successfully.")
            review.delete()
        else:
            messages.error(request, "You can only delete your own reviews!")
    else:
        messages.error(request, "You must be logged in to delete reviews!")
        return redirect('home')

    return redirect('product_item', category=category, product_id=product_id)
