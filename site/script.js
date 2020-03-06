function test(key, a) {
        if(key == "Enter"){
            text = a.value.toUpperCase();
			document.getElementById("groop").innerHTML = text;
            a.value = "";

        }

    }
