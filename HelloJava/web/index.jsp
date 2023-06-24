<%-- 
    Document   : index
    Created on : Jun 24, 2023, 9:27:34 AM
    Author     : franc
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Greetings From Java</title>
        <%
            String message = new String("Hello World!!!");
            
            %>
    </head>
    <body>
        <h1>
            Just popping in to say <% message %>
        </h1>
    </body>
</html>
