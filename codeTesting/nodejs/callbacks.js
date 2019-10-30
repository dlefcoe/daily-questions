

const posts = [
    {title: 'post one', body: 'this is post one'},
    {title: 'post two', body: 'this is post two'}
]


console.log('step 1')


function getPosts() {

    setTimeout(()=>{
        let output = ''
        posts.forEach((post, index)=>{
            output += `<li>${post.title}<\li>`
        })
        //document.body.innerHTML = output
        console.log(output)

    },1000)
    
}

console.log('step 2')

function createPost(post, callback){
    setTimeout(() => {
        console.log('the timeout is done !!')
        posts.push(post)
        callback()
    }, 2000);
    console.log('the timeout is not necesarily done')

}

console.log('step 3')



// getPosts

createPost({title: 'post three', body: 'this is post three'}, getPosts)

