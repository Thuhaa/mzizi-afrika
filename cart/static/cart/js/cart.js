var updateCartBtns = document.getElementsByClassName('update-cart');
for (i=0; i<updateCartBtns.length; i++) {
	updateCartBtns[i].addEventListener('click', function(){
		console.log('Add to Cart Clicked!');
	})
}