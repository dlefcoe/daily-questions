function sync(callback) {
    setTimeout(function(){
        const res = deferred()
        callback(res)
    } ,1000)

    console.log('sync')
    
}

function deferred() {
    return 'deferred'
}


sync((result)=>{
    console.log(result)
})



