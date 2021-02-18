from datetime import date

todays_date = date.today().strftime("%B %d, %Y")

with open("blog/posts.txt", "r") as posts_file:
    posts = [ii.replace("\n", "") for ii in posts_file.readlines()]

n_posts = len(posts)

with open("blog/keywords.txt", "r") as keywords_file:
    keywords = [ii.replace("\n", "") for ii in keywords_file.readlines()]

n_keywords = len(keywords)
n_post_per_keyword = [0] * n_keywords

keyword_blog_pages = []
for ii, keyword in enumerate(keywords):
    keyword_blog_pages.append(open(f"{keyword}.html", "w"))


with open("css/Blogstyle.css", "w") as blog_css_file:
    for ii in range(n_posts):
        blog_css_file.write(f".mySlides{ii + 1} {{display: none}}\n")

with open("js/slideshow.js", "w") as slidshow_js_file:
    slidshow_js_file.write("var slideIndex = [1" + (f",1" * (n_posts - 1)) + "];\n")
    slidshow_js_file.write("var slideId = [" + ', '.join([f'"mySlides{ii + 1}"' for ii in range(n_posts)]) + "]\n\n")
    for ii in range(n_posts):
        slidshow_js_file.write(f"showSlides(1, {ii});\n")
    slidshow_js_file.write("""\n
function plusSlides(n, no) {
  showSlides(slideIndex[no] += n, no);
}

function showSlides(n, no) {
  var i;
  var x = document.getElementsByClassName(slideId[no]);
  if (n > x.length) {slideIndex[no] = 1}
  if (n < 1) {slideIndex[no] = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
  }
  x[slideIndex[no]-1].style.display = "block";
}
""")

blog_nav_bar_from_keywords = '<li> <a class="page-scroll" href=blog.html>Recent</a></li>\n'
for ii, keyword in enumerate(keywords):
    blog_nav_bar_from_keywords += f'<li> <a class="page-scroll" href={keyword}.html>{keyword}</a></li>\n'

blog_nav_bar = f"""
<!-- Navigation -->
<div id="nav">
  <nav class="navbar navbar-custom">
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-main-collapse"> <i class="fa fa-bars"></i> </button>
        <a class="navbar-brand page-scroll" href="index.html">Home</a> </div>

      <!-- Collect the nav links, forms, and other content for toggling -->
      <div class="collapse navbar-collapse navbar-right navbar-main-collapse">
        <ul class="nav navbar-nav">
          <!-- Hidden li included to remove active class from about link when scrolled up past about section -->
          {blog_nav_bar_from_keywords}          
        </ul>
      </div>
    </div>
  </nav>
</div>
"""

#################################################################################
#################################################################################
#################################################################################

blog_header = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CHS Blog</title>
<meta name="description" content="">
<meta name="author" content="">

<!-- Favicons
    ================================================== -->
<link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="apple-touch-icon" sizes="72x72" href="img/apple-touch-icon-72x72.png">
<link rel="apple-touch-icon" sizes="114x114" href="img/apple-touch-icon-114x114.png">

<!-- Bootstrap -->
<link rel="stylesheet" type="text/css"  href="css/bootstrap.css">
<link rel="stylesheet" type="text/css" href="fonts/font-awesome/css/font-awesome.css">

<!-- Stylesheet
    ================================================== -->
<link rel="stylesheet" type="text/css"  href="css/Blogstyle.css">
<link rel="stylesheet" type="text/css"  href="css/CHSstyle.css">
<link rel="stylesheet" type="text/css" href="css/prettyPhoto.css">

<link href='http://fonts.googleapis.com/css?family=Lato:400,700,900,300' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,700,800,600,300' rel='stylesheet' type='text/css'>
<script type="text/javascript" src="js/modernizr.custom.js"></script>

<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
<!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>
<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">

{blog_nav_bar}
"""





blog_footer = f"""
<!--Footer-->
<div id="footer">
  <div class="container text-center">
    <div class="fnav">
      <p>Copyright &copy; 2018 Chateaugay Historical Society. </br>
      Last Modified [{todays_date}]. Designed by Chateaugay Historical Society. Template by <a href="http://www.templatewire.com" rel="nofollow">TemplateWire</a></p>
    </div>
  </div>
</div>
<script type="text/javascript" src="js/jquery.1.11.1.js"></script> 
<script type="text/javascript" src="js/bootstrap.js"></script> 
<script type="text/javascript" src="js/SmoothScroll.js"></script> 
<script type="text/javascript" src="js/easypiechart.js"></script> 
<script type="text/javascript" src="js/jquery.prettyPhoto.js"></script> 
<script type="text/javascript" src="js/jquery.isotope.js"></script> 
<script type="text/javascript" src="js/jquery.counterup.js"></script> 
<script type="text/javascript" src="js/waypoints.js"></script> 
<script type="text/javascript" src="js/jqBootstrapValidation.js"></script> 
<script type="text/javascript" src="js/contact_me.js"></script> 
<script type="text/javascript" src="js/main.js"></script>
<script type="text/javascript" src="js/slideshow.js"></script>
</body>
</html>
"""

for ii, keyword in enumerate(keywords):
    keyword_blog_pages[ii].write(blog_header + "\n")

with open("./blog.html", "w") as mainblog_file:
    mainblog_file.write(blog_header + "\n")
    for ii in range(n_posts):
        with open(f"blog/post_source/{posts[ii]}.txt", "r") as post_source_file:
            post_source = [jj.replace("\n", "") for jj in post_source_file.readlines()]

        content_filename = post_source[0]
        image_filename = post_source[1]

        this_title = post_source[2]
        this_author = post_source[3]
        this_date = post_source[4]

        this_keywords = post_source[5:]
        n_this_keywords = len(this_keywords)

        with open(f"blog/imgs/{posts[ii]}/{image_filename}", "r") as image_file:
            images = [jj.replace("\n", "") for jj in image_file.readlines()]

        n_images = len(images)

        with open(f"blog/content/{content_filename}", "r") as content_file:
            content = [jj.replace("\n", "") for jj in content_file.readlines()]

        content = "\n".join(content)

        if ii <= 2:
            mainblog_file.write(f"""
<!-- Site Page -->
<div id="blog{ii%2 + 1}">
  <div class="container">
    <div class="section-title text-center center">
      <h2>{this_title}</h2>
      <hr>
      <h5>{this_date} | {this_author}</h5>
    </div>

     <!-- Slideshow container -->
<div class="slideshow-container">

<!-- Full-width images with number and caption text -->

""")

            for kk in range(n_images):
                mainblog_file.write(f"""
  <div class="mySlides{ii + 1} none">
     <div class="numbertext">{kk + 1} / {n_images}</div>
    <img src="blog/imgs/{posts[ii]}/{images[kk]}" style="width:100%">
  </div>
"""+ "\n")
            mainblog_file.write(f"""
      <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1, {ii})">&#10094;</a>
  <a class="next" onclick="plusSlides(1, {ii})">&#10095;</a>
</div>
<br>
""" + "\n")
            mainblog_file.write(f"""
        <div class="blog-text">
        {content}
        </div>
    </div>
</div>
""" + "\n")

        for ll in range(n_keywords):
            current_blog_keyword = keywords[ll]
            if current_blog_keyword in this_keywords:
                keyword_blog_pages[ll].write(f"""
<!-- Site Page -->
<div id="blog{ii%2 + 1}">
  <div class="container">
    <div class="section-title text-center center">
      <h2>{this_title}</h2>
      <hr>
      <h5>{this_date} | {this_author}</h5>
    </div>

     <!-- Slideshow container -->
<div class="slideshow-container">

<!-- Full-width images with number and caption text -->

""")

                for kk in range(n_images):
                    keyword_blog_pages[ll].write(f"""
  <div class="mySlides{n_post_per_keyword[ll] + 1} none">
     <div class="numbertext">{kk + 1} / {n_images}</div>
    <img src="blog/imgs/{posts[ii]}/{images[kk]}" style="width:100%">
  </div>
""" + "\n")
                keyword_blog_pages[ll].write(f"""
      <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1, {n_post_per_keyword[ll]})">&#10094;</a>
  <a class="next" onclick="plusSlides(1, {n_post_per_keyword[ll]})">&#10095;</a>
</div>
<br>
""" + "\n")
                keyword_blog_pages[ll].write(f"""
        <div class="blog-text">
        {content}
        </div>
    </div>
</div>
""" + "\n")
                n_post_per_keyword[ll] += 1

    mainblog_file.write(blog_footer + "\n")

for ii, keyword in enumerate(keywords):
    keyword_blog_pages[ii].write(blog_footer + "\n")
    keyword_blog_pages[ii].close()
