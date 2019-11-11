function getRating() {
    //this function is getting the text value of a movies rating from the dom.
    var value = $("#star-rating").text();
    //it converts it to a number
    var n = Number(value);
    var rating = '';
    //it adds a materialise icon for the appropriate amount into the var rating 
    for (n; n > 0; n--) {
        rating += '<i class="material-icons">star</i>';
    }
    //and replaces the original value with stars!
    $("#star-rating").html(rating);
};
getRating();