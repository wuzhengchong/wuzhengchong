function getSource() {
      var objHtml = document.documentElement;
      document.getElementById("txtarea").value = "<"+ objHtml.nodeName
      + ">" + objHtml.innerHTML + "</" + objHtml.nodeName + ">";
    }
