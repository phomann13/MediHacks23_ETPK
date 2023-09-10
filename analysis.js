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

//stores all objects from JSON file into posts and all ratings into their respective 2d array
for (i = 0; i < sample.length; i ++) {
    array[i] = JSON.stringify(sample[i]);
    posts[i] = JSON.parse(array[i]);
    if (res_ratings[posts[i].inst_name] == undefined){
        res_ratings[posts[i].inst_name] = [parseInt(posts[i].res_rating)];
    } else {
        res_ratings[posts[i].inst_name][res_ratings[posts[i].inst_name].length] = parseInt(posts[i].res_rating);
    }

    if (cult_ratings[posts[i].inst_name] == undefined){
        cult_ratings[posts[i].inst_name] = [parseInt(posts[i].cult_rating)];
    } else {
        cult_ratings[posts[i].inst_name][cult_ratings[posts[i].inst_name].length] = parseInt(posts[i].cult_rating);
    }
}

//returns average of culture ratings for the input school 
// param: school string
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

//returns average of resource ratings for the input school 
// param: school string
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

//returns lowest of culture ratings for the input school 
// param: school string
function get_school_cult_lowest(school){
    if (cult_ratings[school] == undefined) {
        return undefined; 
    }
    let arr = cult_ratings[school].sort(); 
    return arr[0];
}

//returns highest of culture ratings for the input school 
// param: school string
function get_school_cult_highest(school){
    if (cult_ratings[school] == undefined) {
        return undefined; 
    }
    let arr = cult_ratings[school].sort(); 
    return arr[cult_ratings[school].length - 1];
}

//returns lowest of resource ratings for the input school 
// param: school string
function get_school_res_lowest(school){
    if (res_ratings[school] == undefined) {
        return undefined; 
    }
    let arr = res_ratings[school].sort(); 
    return arr[0];
}

//returns highest of resource ratings for the input school 
// param: school string
function get_school_res_highest(school){
    if (res_ratings[school] == undefined) {
        return undefined; 
    }
    let arr = res_ratings[school].sort(); 
    return arr[res_ratings[school].length - 1];
}

console.log(get_school_res_highest("XYZ"));