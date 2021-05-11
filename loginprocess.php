<?php
 $con=mysqli_connect("localhost","root","") or die("error".mysqli_error());
 $selectdb=mysqli_select_db($con,"criminal") or die("error".mysqli_error());
 $email=$_POST["email"];
 $password=$_POST["password"];
 $query="select * from register where email='$email' && password='$password'";
 $execute=mysqli_query($con,$query) or die("error".mysqli_error());
 if(mysqli_num_rows($execute)>0)
 {
     ?>
     <script language="javascript">
        //  alert("success");
         window.location.replace('home.html');
         </script>
         <?php
 }
 else{
     ?>
     <script language="javascript">
         alert("invalid password or email");
         window.location.replace("index.html");
         </script>
         <?php
 }    
 ?>

