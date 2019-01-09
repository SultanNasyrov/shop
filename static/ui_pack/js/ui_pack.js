$(document).ready(function () {

    // PRODUCT
    const product = $('.product');
    product.mouseenter(function () {
        console.log('mouse entered the product');
        let image = $(this).find('.product-image');
        console.log(image);
        let imageCaption = $(this).find('.product-image-caption');

        TweenMax.to(image, 3, {scale: 1.1});
        TweenMax.to(imageCaption, 1, {opacity: 1})
    });

    product.mouseleave(function () {
        console.log('mouse left the product');
        let image = $(this).find('.product-image');
        let imageCaption = $(this).find('.product-image-caption');

        TweenMax.to(image, 1, {scale: 1});
        TweenMax.to(imageCaption, 0.5, {opacity: 0})
    });


})