function Search() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchBar");
    filter = input.value.toUpperCase();
    table = document.getElementById("class-table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
      //specifies what data to search for
      td = tr[i].getElementsByTagName("td")[1];
      classType = tr[i].getElementsByTagName("td")[3];
      if (td || classType) {
        //.textContent allows searching of hidden spans which can be used as filters. Class types will be the main filters however textContent allows us to create specific filters whenever needed
        txtValue = td.textContent;
        txtValueType = classType.textContent;
        //txtValueType allows the user to search by class type and is intuitive due to the information being displayed both on the table and search box. It's also easy to add any additional search columns such as GPA weight if we decide to.
        if (
          txtValue.toUpperCase().indexOf(filter) > -1 ||
          txtValueType.toUpperCase().indexOf(filter) > -1
        ) {
          //if the characters in the input match certain characters in the table, it will display the matches.
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }