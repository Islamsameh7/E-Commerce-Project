var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
updateBtns[i].addEventListener('click', function(){
    var productName = this.dataset.product
    var action = this.dataset.action
    console.log('Product name: ', productName, ' action: ', action)

    console.log('User: ', user)
    if(user === 'AnonymousUser'){
        alert('Please login to access your cart.')
        
    }else{
        updateUserOrder(productName, action)
    }
})
}

function updateUserOrder(productName, action){

    var url = 'update_item'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'applicationjson',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({'productName': productName, 'action': action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        alert('Item added succesfully')
        location.reload()
    })
}