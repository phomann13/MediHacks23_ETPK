/** Post: 
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
let array = [];
let posts = [];
let res_ratings = []; 
let cult_ratings = []; 

//stores all objects from JSON file into posts
for (i = 0; i < sample.length; i ++) {
    array[i] = JSON.stringify(sample[i]);
    posts[i] = JSON.parse(array[i]);
    if (res_ratings[posts[i].inst_name] == undefined){
        res_ratings[posts[i].inst_name] = [parseInt(posts[i].res_rating)];
    } else {
        res_ratings[posts[i].inst_name][res_ratings[posts[i].inst_name].length] = parseInt(posts[i].res_rating);
    }

    if (cult_ratings[posts[i].inst_name] == undefined){
        console.log("1");
        cult_ratings[posts[i].inst_name] = [parseInt(posts[i].cult_rating)];
    } else {
        console.log("2");
        cult_ratings[posts[i].inst_name][cult_ratings[posts[i].inst_name].length] = parseInt(posts[i].cult_rating);
    }
}

function get_school_cult_avg(school){
    let sum = 0, count = cult_ratings[school].length;
    if (count == 0) {
        return 0;
    }

    for (i = 0; i < count; i++){
        sum = sum + cult_ratings[school][i];
    }
    return sum/count; 
}

function get_school_res_avg(school){
    let sum = 0, count = res_ratings[school].length;
    if (count == 0) {
        return 0;
    }

    for (i = 0; i < count; i++){
        sum = sum + res_ratings[school][i];
    }
    return sum/count; 
}

console.log(get_school_cult_avg("UVA"));