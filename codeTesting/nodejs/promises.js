

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

function createPost(post){
    return new Promise((resolve, reject)=>{

        setTimeout(() => {
            console.log('the timeout is done !!')
            posts.push(post)

            const error = false

            if (!error) {
                resolve()
            } else {
                reject('error: something went wrong')
            }
            

        }, 2000);
        console.log('the timeout is not necesarily done')
    })

}


console.log('step 3')

createPost({title: 'post three', body: 'this is post three'})
    .then(getPosts)
    .catch(err => console.log(err))


console.log('step 4')



