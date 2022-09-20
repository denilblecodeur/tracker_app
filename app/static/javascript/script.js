function getValue()
{
    var element = [];
    element[0] = document.getElementById("url").value;
    element[1] = document.getElementById("prix").value.replace(/,/g, ".").replace(/€/g, "");
    element[2] = document.getElementById("email").value;
    for (el of element)
    {
        if (el == '')
        {
            alert('Merci de remplir tous les champs !');
            return
        }
    }
    if(!validURL(element[0]))
    {
        alert('URL non valide');
    }
    else if(isNaN(element[1])==true)
    {
        alert(element[1]+' n\'est pas un nombre');
    }
    else if(!validEmail(element[2]))
    {
        alert('Adresse mail non reconnue');
    }
    else
    {
        document.getElementById("submit_button").style.display = "none";
        document.getElementById("retour_affiche").style.display = "block";
        var dic = {'url': element[0],'price': element[1],'email':element[2]};
        $.ajax(
            {
            type: "POST",
            contentType: "application/json; charset=utf-8",
            url: "/",
            data: JSON.stringify(dic),
            dataType: "json",
            success:function(response)
            {
                document.getElementById("ifr").style.display = "none";
                document.getElementById("returned").style.display = "block";
                document.getElementById("returned").innerText = response.retour;
                document.getElementById("reset_button").style.display = "block";
            }   
        });
    }
}

function validURL(str_url)
{
    var a  = document.createElement('a');
    a.href = str_url;
    return (a.host && a.host != window.location.host);
}

function validEmail(email) 
{
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}
function reload_page()
{
    /* To reload the page keeping the POST data, use: */
    /* window.location.reload(); */
    /* To reload the page discarding the POST data (perform a GET request), use: */
    window.location.href = window.location.href;

}