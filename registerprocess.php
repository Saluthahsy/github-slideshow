<?php
 $con=mysqli_connect("localhost","root","") or die("error".mysqli_error());
 $selectdb=mysqli_select_db($con,"criminal") or die("error");
 $name=$_POST["name"];
 $ph=$_POST["phoneno"];
 $age=$_POST["age"];
 $email=$_POST["email"];
 $password=$_POST["password"];
 $query="insert into register values('','$name','$ph','$age','$email','$password')";
 $execute=mysqli_query($con,$query) or die("error".mysqli_error());
 if($execute)
 {
     ?>
     <script language="javascript">
         alert("success");
         window.location.replace("index.html");
         </script>
         <?php
 }
 else{
     ?>
     <script language="javascript">
         alert("your registration is failed please do again");
         window.location.replace("register.html");
         </script>
         <?php
 }    
 ?>



 