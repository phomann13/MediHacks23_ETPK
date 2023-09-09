function univ_sign(){
   
    document.getElementById("univ").style.display = "block"
    document.getElementById('indiv_nfirst').style.display = "none"
    document.getElementById('indiv_nlast').style.display = "none"
}

function indiv_sign(){
    document.getElementById('indiv_nfirst').style.display = "block"
    document.getElementById('indiv_nlast').style.display = "block"
    document.getElementById("univ").style.display = "none"

}