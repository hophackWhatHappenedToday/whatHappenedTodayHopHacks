function makeList(listData){
    var list = document.createElement('ul');

        for (var i = 0; i < array.length; i++) {
            // Create the list item:
            var item = document.createElement('li');

            // Set its contents:
            item.appendChild(document.createTextNode(listData[i]));

            // Add it to the list:
            list.appendChild(item);
    }

    // Finally, return the constructed list:
    return list;
}