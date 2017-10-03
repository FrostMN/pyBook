
function addFilter(event) {
    if (event.keyCode == 13) {
        var typeSelector = document.getElementById("search-type");

        var type = typeSelector.options[typeSelector.selectedIndex].value;
        var typeText = typeSelector.options[typeSelector.selectedIndex].innerHTML;
        //alert("in addFilter()");
        //alert(typeText + ": " + type);

        var filter = document.createElement('div');
        var searchParam = document.getElementById('searchTXT').value;
        filter.setAttribute("id", "filter-" + type + "-" + searchParam);
        filter.setAttribute("class", "filter filter-on");
        var list = document.createElement('ul');
        var name = document.createElement('li');
        var close = document.createElement('li');
        var closeLink = document.createElement('a');
        var closeIcon = document.createElement('i');
        name.setAttribute("class", "left");
        name.innerHTML = typeText + ": " + searchParam;
        close.setAttribute("class", "right");
        closeLink.setAttribute("onclick", "deleteFilter(this.parentNode)");
        closeLink.setAttribute("href", "javascript:void(0)");
        closeIcon.setAttribute("class", "fa fa-times");
        closeIcon.setAttribute("aria-hidden", "true");
        closeLink.appendChild(closeIcon);
        document.getElementById('filters').appendChild(filter);
        close.appendChild(closeLink);
        list.appendChild(name);
        list.appendChild(close);
        filter.appendChild(list);
        var filters = document.getElementById('filters');
        filters.appendChild(filter);

        //var type = "Author";
        //var type = "Title";
        //alert("before filter()");

        filterBooks(type, searchParam);
    }
}

function deleteFilter(obj) {
    //alert('just alert');
    //window.alert("before elem");
    var elem = document.getElementById(obj.parentNode.parentNode.id);
    //window.alert("before remove");
    elem.parentNode.removeChild(elem);
    unfilter()
}

function unfilter() {
    var filters = document.getElementById('filters');

    if ( filters.childElementCount < 1 ){
        unfilterAll();
    }
}


function unfilterAll() {
    //alert('in unfilterAll');
    var shelf = document.getElementById('container').childNodes;
    var books = shelf[1].childNodes;

    for (var i = 0; i < books.length; i++ ) {
        //window.alert("books[" + i + "]: " + books[i].className);
        if (books[i].tagName == "DIV") {
            //alert("its a div");
            if (books[i].classList.contains("filtered")) {
                books[i].classList.remove("filtered");
               // alert("filtered")
            }
        }
    }
}

function filterBooks(type, searchParam) {
    //alert("in filter()");
    var shelf = document.getElementById('container').childNodes;
    var books = shelf[1].childNodes;

    for ( var i = 0; i < books.length; i++ ) {
        if ( books[i].tagName == "DIV" ) {
            if (type == "author") {
                //alert("its a div and type author");
                filterByAuthor(searchParam, books[i])
            }

            if (type == "title") {
                //alert("its a div and type author");
                filterByTitle(searchParam, books[i])
            }
        }
    }

}

function filterByAuthor( filterParam , book) {
    //alert("in filter by author" + book);
    for (var i = 0; i < book.childNodes.length; i++) {
        //alert(book.childNodes[i].tagName + " " + book.childNodes[i].classList);
        if (book.childNodes[i].tagName == "DIV" && book.childNodes[i].classList == "book-text") {
            //alert("in DIV and book-text")
            var textElem = book.childNodes[i].childNodes;
            //alert(textElem);
            for (var j = 0; j < textElem.length; j++) {
                //alert(textElem[j].tagName);
                if (textElem[j].tagName == "H4") {
                    var author = textElem[j].innerHTML;
                    //alert("found author:" + author);
                    //alert("found filterParam:" + filterParam);
                    if (author.indexOf(filterParam)) {
                        //alert("in filter if");
                        book.classList.add("filtered");
                    }
                }
            }
        }
    }
}

function filterByTitle( filterParam , book) {
    //alert("in filter by title" + book);
    for (var i = 0; i < book.childNodes.length; i++) {
        //alert(book.childNodes[i].tagName + " " + book.childNodes[i].classList);
        if (book.childNodes[i].tagName == "DIV" && book.childNodes[i].classList == "book-text") {
            //alert("in DIV and book-text")
            var textElem = book.childNodes[i].childNodes;
            //alert(textElem);
            for (var j = 0; j < textElem.length; j++) {
                //alert(textElem[j].tagName);
                if (textElem[j].tagName == "H2") {
                    var title = textElem[j].innerHTML;
                    //alert("found title:" + title);
                    //alert("found filterParam:" + filterParam);
                    //alert(title.indexOf(filterParam));
                    if (title.indexOf(filterParam) < 0) {
                        //alert("in filter if");

                        book.classList.add("filtered");
                    }
                }
            }
        }
    }
}


function hideBook(bookID) {
    var book = document.getElementById(bookID);
    book.classList.add("hidden");
    addHideFilter();
}

function unhide() {
    var shelf = document.getElementById('container').childNodes;
    var books = shelf[1].childNodes;

        for (var i = 0; i < books.length; i++ ) {
        //window.alert("books[" + i + "]: " + books[i].className);
        if (books[i].tagName == "DIV") {
            //alert("its a div");
            if (books[i].classList.contains("hidden")) {
                books[i].classList.remove("hidden");
               // alert("filtered")
            }
        }
    }

    var hiddenFilter = document.getElementById("hide-books");
    var filterCon = document.getElementById("filters");

    filterCon.removeChild(hiddenFilter);

}

function addHideFilter() {
    var noneHidden = true;

    var filter_container = document.getElementById("filters");
    var filter_count = filter_container.childElementCount;

    if (filter_count > 0) {
        var filt = filter_container.childNodes;

        for (var i = 0; i < filt.length; i++) {
            if (filt[i].tagName == "DIV") {
                if (filt[i].getAttribute("id") == "hide-books") {
                    noneHidden = false;
                }
            }
        }

    }

    if (noneHidden) {
        var hide = document.createElement('div');
        hide.setAttribute("id", "hide-books");
        hide.setAttribute("class", "filter filter-on");
        var list = document.createElement('ul');
        var name = document.createElement('li');
        var close = document.createElement('li');
        var closeLink = document.createElement('a');
        var closeIcon = document.createElement('i');
        name.setAttribute("class", "left");
        name.innerHTML = "Hidden ";
        close.setAttribute("class", "right");
        closeLink.setAttribute("onclick", "unhide()");
        closeLink.setAttribute("href", "javascript:void(0)");
        closeIcon.setAttribute("class", "fa fa-times");
        closeIcon.setAttribute("aria-hidden", "true");
        closeLink.appendChild(closeIcon);
        document.getElementById('filters').appendChild(hide);
        close.appendChild(closeLink);
        list.appendChild(name);
        list.appendChild(close);
        hide.appendChild(list);
        var filters = document.getElementById('filters');
        filters.appendChild(hide);
    }
}
