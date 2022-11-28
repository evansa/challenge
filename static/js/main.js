    function required()
    {
        var empt = document.forms["form1"]["guess"].value;
        if (empt == "")
        {
            alert("Please enter the capital");
            return false;
        }    
            return true; 
    }