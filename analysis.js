/**
 * Post: 
 * {
 *  title: string,
 *  inst_name: string,
 *  cult_rating: int,
 *  res_rating: int,
 *  cult_comment: string,
 *  res_comment: string
 * }
 */


//sample contains all from the JSON as an array of post objects
const sample = require('./storage.json');
array = [];
posts = [];

//stores all objects from JSON file into posts
for (i = 0; i < sample.length; i ++) {
    array[i] = JSON.stringify(sample[i]);
    posts[i] = JSON.parse(array[i]);
}

console.log(posts[1].title);