<?php
 $con=mysqli_connect("localhost","root","") or die("error".mysqli_error());
 $selectdb=mysqli_select_db($con,"criminal") or die("error");
 $name=$_POST["name"];
 $feedback=$_POST["feedback"];
 $query="insert into feedbacks values('','$name','$feedback')";
 $execute=mysqli_query($con,$query) or die("error".mysqli_error($con));
 if($execute)
 {
     ?>
     <script language="javascript">
         alert("success");
         window.location.replace("home.html");
         </script>
         <?php
 }
 else{
     ?>
     <script language="javascript">
         alert("your feedback is failed please do again");
         window.location.replace("feedback.html");
         </script>
         <?php
 }    
 ?>
