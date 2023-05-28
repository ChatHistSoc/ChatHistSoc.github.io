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
    keyword_blog_pages.append(open(f"blog/pages/{keyword}.html", "w"))

#################################################################################
#################################################################################
#################################################################################

def blog_header(keyword):
    return f"""
<!DOCTYPE html>
<html style="font-size: 16px;" lang="en"><head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="keywords" content="">
    <meta name="description" content="">
    <title>CHS Blog - {keyword.replace('_', ' ')}</title>
    <link rel="stylesheet" href="../../css/nicepage.css" media="screen">
    <link rel="stylesheet" href="../../css/BlogTemplate.css" media="screen">
    <script class="u-script" type="text/javascript" src="../../js/jquery.js" defer=""></script>
    <script class="u-script" type="text/javascript" src="../../js/nicepage.js" defer=""></script>
    <meta name="generator" content="Nicepage 4.18.5, nicepage.com">
    
    
    
    <script type="application/ld+json">{{
        "@context": "http://schema.org",
        "@type": "Organization",
        "name": "CHS-Website",
        "logo": "../../images/CHSLOGO-white.png",
        "sameAs": [
                "https://www.facebook.com/profile.php?id=100057393972683"
        ]
}}</script>
    <meta name="theme-color" content="#478ac9">
    <meta property="og:title" content="">
    <meta property="og:description" content="">
    <meta property="og:type" content="website">
    <meta data-intl-tel-input-cdn-path="intlTelInput/">
  </head>
  <body class="u-body u-xl-mode" data-lang="en"><header class="u-clearfix u-grey-80 u-header u-sticky u-sticky-7f93 u-header" id="sec-d9a5"><div class="u-clearfix u-sheet u-sheet-1">
        <a href="../../index.html" class="u-image u-logo u-image-1" data-image-width="2320" data-image-height="1659" title="Home">
          <img src="../../images/CHSLOGO-white.png" class="u-logo-image u-logo-image-1">
        </a>
        <nav class="u-menu u-menu-dropdown u-offcanvas u-menu-1">
          <div class="menu-collapse" style="font-size: 1rem; letter-spacing: 0px; font-weight: 400;">
            <a class="u-button-style u-custom-active-color u-custom-hover-color u-custom-left-right-menu-spacing u-custom-padding-bottom u-custom-text-active-color u-custom-text-hover-color u-custom-text-shadow u-custom-top-bottom-menu-spacing u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="#" style="font-size: calc(1em + 8px);">
              <svg class="u-svg-link" viewBox="0 0 24 24"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#menu-hamburger"></use></svg>
              <svg class="u-svg-content" version="1.1" id="menu-hamburger" viewBox="0 0 16 16" x="0px" y="0px" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg"><g><rect y="1" width="16" height="2"></rect><rect y="7" width="16" height="2"></rect><rect y="13" width="16" height="2"></rect>
</g></svg>
            </a>
          </div>
          <div class="u-custom-menu u-nav-container">
            <ul class="u-nav u-unstyled u-nav-1"><li class="u-nav-item"><a class="u-active-grey-70 u-button-style u-hover-grey-70 u-nav-link u-text-active-white u-text-hover-white" href="../../index.html" style="padding: 10px 20px;">Home</a>
</li><li class="u-nav-item"><a class="u-active-grey-70 u-button-style u-hover-grey-70 u-nav-link u-text-active-white u-text-hover-white" href="../../About.html" style="padding: 10px 20px;">About</a><div class="u-nav-popup"><ul class="u-h-spacing-20 u-nav u-unstyled u-v-spacing-10 u-nav-2"><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../About.html#sec-60ec">Mission</a>
</li><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../About.html#sec-6645">Governance</a>
</li><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../About.html#sec-236c">Get Involved</a><div class="u-nav-popup"><ul class="u-h-spacing-20 u-nav u-unstyled u-v-spacing-10 u-nav-3"><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../About.html#sec-236c">Membership</a>
</li><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../About.html#sec-236c">Volunteer</a>
</li><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../About.html#sec-236c">Donate</a>
</li></ul>
</div>
</li><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../About.html#sec-577b">Newsletter</a>
</li></ul>
</div>
</li><li class="u-nav-item"><a class="u-active-grey-70 u-button-style u-hover-grey-70 u-nav-link u-text-active-white u-text-hover-white" href="../../Learn.html" style="padding: 10px 20px;">Learn</a><div class="u-nav-popup"><ul class="u-h-spacing-20 u-nav u-unstyled u-v-spacing-10 u-nav-4"><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../Blog.html">Blog</a>
</li><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../Collections-and-Research.html">Collections and Research</a>
</li><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../Exhibits.html">Exhibits</a>
</li><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../Local-Tours.html">Local Tours</a>
</li><li class="u-nav-item"><a class="u-button-style u-hover-palette-5-light-2 u-nav-link u-white" href="../../Resources.html">Resources</a>
</li></ul>
</div>
</li><li class="u-nav-item"><a class="u-active-grey-70 u-button-style u-hover-grey-70 u-nav-link u-text-active-white u-text-hover-white" href="../../Calendar-of-Events.html" style="padding: 10px 20px;">Calendar of Events</a>
</li><li class="u-nav-item"><a class="u-active-grey-70 u-button-style u-hover-grey-70 u-nav-link u-text-active-white u-text-hover-white" href="../../index.html#carousel_ea16" style="padding: 10px 0px 10px 20px;">Contact and Visit</a>
</li></ul>
          </div>
          <div class="u-custom-menu u-nav-container-collapse">
            <div class="u-container-style u-grey-80 u-inner-container-layout u-opacity u-opacity-95 u-sidenav">
              <div class="u-inner-container-layout u-sidenav-overflow">
                <div class="u-menu-close"></div>
                <ul class="u-align-center u-nav u-popupmenu-items u-text-active-white u-text-hover-palette-5-dark-1 u-text-palette-5-light-1 u-unstyled u-nav-5"><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../index.html">Home</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../About.html">About</a><div class="u-nav-popup"><ul class="u-h-spacing-20 u-nav u-unstyled u-v-spacing-10 u-nav-6"><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../About.html#sec-60ec">Mission</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../About.html#sec-6645">Governance</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../About.html#sec-236c">Get Involved</a><div class="u-nav-popup"><ul class="u-h-spacing-20 u-nav u-unstyled u-v-spacing-10 u-nav-7"><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../About.html#sec-236c">Membership</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../About.html#sec-236c">Volunteer</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../About.html#sec-236c">Donate</a>
</li></ul>
</div>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../About.html#sec-577b">Newsletter</a>
</li></ul>
</div>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../Learn.html">Learn</a><div class="u-nav-popup"><ul class="u-h-spacing-20 u-nav u-unstyled u-v-spacing-10 u-nav-8"><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../Blog.html">Blog</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../Collections-and-Research.html">Collections and Research</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../Exhibits.html">Exhibits</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../Local-Tours.html">Local Tours</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../Resources.html">Resources</a>
</li></ul>
</div>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../Calendar-of-Events.html">Calendar of Events</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="../../index.html#carousel_ea16">Contact and Visit</a>
</li></ul>
              </div>
            </div>
            <div class="u-grey-80 u-menu-overlay u-opacity u-opacity-10"></div>
          </div>
        </nav>
      </div></header>
"""

#################################################################################
#################################################################################
#################################################################################

blog_footer = f"""
    <footer class="u-align-center-md u-align-center-sm u-align-center-xs u-clearfix u-footer u-grey-80" id="sec-3241"><div class="u-clearfix u-sheet u-sheet-1">
        <a href="../../index.html" class="u-image u-logo u-image-1" data-image-width="2320" data-image-height="1659" title="Home">
          <img src="../../images/CHSLOGO-white.png" class="u-logo-image u-logo-image-1">
        </a>
        <div class="u-align-left-lg u-align-left-md u-align-left-sm u-align-left-xl u-align-right-xs u-social-icons u-spacing-10 u-social-icons-1">
          <a class="u-social-url" title="facebook" target="_blank" href="https://www.facebook.com/profile.php?id=100057393972683"><span class="u-icon u-social-facebook u-social-icon u-icon-1"><svg class="u-svg-link" preserveAspectRatio="xMidYMin slice" viewBox="0 0 112 112" style=""><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg-3427"></use></svg><svg class="u-svg-content" viewBox="0 0 112 112" x="0" y="0" id="svg-3427"><circle fill="currentColor" cx="56.1" cy="56.1" r="55"></circle><path fill="#FFFFFF" d="M73.5,31.6h-9.1c-1.4,0-3.6,0.8-3.6,3.9v8.5h12.6L72,58.3H60.8v40.8H43.9V58.3h-8V43.9h8v-9.2
            c0-6.7,3.1-17,17-17h12.5v13.9H73.5z"></path></svg></span>
          </a>
        </div>
        <p class="u-align-center-lg u-align-center-md u-align-center-xl u-align-center-xs u-text u-text-1">© 2023 Chateaugay Historical Society<br> Designed by Chateaugay Historical Society using <a href="https://nicepage.com/html-templates" class="u-active-none u-border-none u-btn u-button-link u-button-style u-hover-none u-none u-text-palette-1-base u-btn-1" target="_blank">nicepage</a>
          <br>Last Modified {todays_date}.<br>
        </p>
      </div></footer>
    <section class="u-backlink u-clearfix u-grey-80">
      <a class="u-link" href="https://nicepage.com/website-templates" target="_blank">
        <span>Website Templates</span>
      </a>
      <p class="u-text">
        <span>created with</span>
      </p>
      <a class="u-link" href="" target="_blank">
        <span>Website Builder Software</span>
      </a>. 
    </section>
"""
#################################################################################
#################################################################################
#################################################################################

def make_content(content, ii):
    #Carousel Navigation, then Content
    return f"""
          </div>
          <a class="u-absolute-vcenter u-carousel-control u-carousel-control-prev u-grey-70 u-icon-circle u-opacity u-opacity-70 u-spacing-10 u-text-white u-carousel-control-1" href="#carousel-{ii+1}" role="button" data-u-slide="prev">
            <span aria-hidden="true">
              <svg viewBox="0 0 451.847 451.847"><path d="M97.141,225.92c0-8.095,3.091-16.192,9.259-22.366L300.689,9.27c12.359-12.359,32.397-12.359,44.751,0
c12.354,12.354,12.354,32.388,0,44.748L173.525,225.92l171.903,171.909c12.354,12.354,12.354,32.391,0,44.744
c-12.354,12.365-32.386,12.365-44.745,0l-194.29-194.281C100.226,242.115,97.141,234.018,97.141,225.92z"></path></svg>
            </span>
            <span class="sr-only">
              <svg viewBox="0 0 451.847 451.847"><path d="M97.141,225.92c0-8.095,3.091-16.192,9.259-22.366L300.689,9.27c12.359-12.359,32.397-12.359,44.751,0
c12.354,12.354,12.354,32.388,0,44.748L173.525,225.92l171.903,171.909c12.354,12.354,12.354,32.391,0,44.744
c-12.354,12.365-32.386,12.365-44.745,0l-194.29-194.281C100.226,242.115,97.141,234.018,97.141,225.92z"></path></svg>
            </span>
          </a>
          <a class="u-absolute-vcenter u-carousel-control u-carousel-control-next u-grey-70 u-icon-circle u-opacity u-opacity-70 u-spacing-10 u-text-white u-carousel-control-2" href="#carousel-{ii+1}" role="button" data-u-slide="next">
            <span aria-hidden="true">
              <svg viewBox="0 0 451.846 451.847"><path d="M345.441,248.292L151.154,442.573c-12.359,12.365-32.397,12.365-44.75,0c-12.354-12.354-12.354-32.391,0-44.744
L278.318,225.92L106.409,54.017c-12.354-12.359-12.354-32.394,0-44.748c12.354-12.359,32.391-12.359,44.75,0l194.287,194.284
c6.177,6.18,9.262,14.271,9.262,22.366C354.708,234.018,351.617,242.115,345.441,248.292z"></path></svg>
            </span>
            <span class="sr-only">
              <svg viewBox="0 0 451.846 451.847"><path d="M345.441,248.292L151.154,442.573c-12.359,12.365-32.397,12.365-44.75,0c-12.354-12.354-12.354-32.391,0-44.744
L278.318,225.92L106.409,54.017c-12.354-12.359-12.354-32.394,0-44.748c12.354-12.359,32.391-12.359,44.75,0l194.287,194.284
c6.177,6.18,9.262,14.271,9.262,22.366C354.708,234.018,351.617,242.115,345.441,248.292z"></path></svg>
            </span>
          </a>

        </div>
        <p class="u-align-center u-text u-text-5">To view full size images and read captions, click on an image.</p>
        <p class="u-align-center u-text u-text-3">{content}</p>
      </div>
    </section>
"""
#################################################################################
#################################################################################
#################################################################################

def make_post_title_section(ii, this_title, this_date, this_author, color_selector_string):
    return f"""
    <section class="u-clearfix {color_selector_string} u-section-{ii%2 + 1}" id="sec-{ii+1}">
      <div class="u-clearfix u-sheet u-sheet-{ii%2 + 1}">
        <h3 class="u-align-center u-text u-text-default u-title u-text-1">{this_title}</h3>
        <div class="u-align-center u-border-5 u-border-custom-color-1 u-line u-line-horizontal u-line-1"></div>
        <h5 class="u-align-center u-text u-text-default u-text-2">{this_date} | {this_author}</h5>
        <div class="u-carousel u-expanded-width-xs u-gallery u-gallery-slider u-layout-carousel u-lightbox u-no-transition u-show-text-none u-thumbnails-position-bottom u-gallery-1" id="carousel-{ii+1}" data-interval="5000" data-u-ride="carousel">
          <ol class="u-absolute-hcenter u-carousel-indicators u-carousel-indicators-1">
"""

#################################################################################
#################################################################################
#################################################################################

def make_img_carousel(n_images, ii, posts, images, captions):
    output = f""
    for kk in range(n_images):
        if kk == 0:
            active_string = 'u-active'
        else:
            active_string = ''
        output += f"""<li data-u-target="#carousel-{ii+1}" data-u-slide-to="{kk}" class="{active_string} u-grey-70 u-shape-circle" style="width: 10px; height: 10px;"></li>"""
    
    output += f"""
          </ol>
          <div class="u-carousel-inner u-gallery-inner" role="listbox">"""
    for kk in range(n_images):
        if kk == 0:
            active_string = 'u-active'
        else:
            active_string = ''
        output += f"""
            <div class="{active_string} u-carousel-item u-gallery-item u-carousel-item-{kk+1}">
              <div class="u-back-slide">
                <img class="u-back-image u-expanded" src="../imgs_web/{posts[ii]}/{images[kk]}">
              </div>
              <div class="u-align-center u-over-slide u-valign-bottom u-over-slide-{kk+1}">
                <h3 class="u-gallery-heading" style="width: 618px; margin-right: auto; margin-left: auto;">{captions[kk]}</h3>
                <p class="u-gallery-text" style="width: 618px; margin-right: auto; margin-left: auto;">{""}</p>
              </div>
            </div>
"""
    return output

#################################################################################
#################################################################################
#################################################################################

for ii, keyword in enumerate(keywords):
    keyword_blog_pages[ii].write(blog_header(keyword) + "\n")


with open("./blog/pages/Recent.html", "w") as recentblog_file:
    recentblog_file.write(blog_header('Recent') + "\n")
    for ii in range(n_posts):
        with open(f"blog/post_source/{posts[ii]}.txt", "r") as post_source_file:
            post_source = [jj.replace("\n", "") for jj in post_source_file.readlines()]

        content_filename = post_source[0]
        image_filename = post_source[1]
        caption_filename = post_source[2]

        this_title = post_source[3]
        this_author = post_source[4]
        this_date = post_source[5]

        this_keywords = post_source[6:]
        n_this_keywords = len(this_keywords)

        with open(f"blog/imgs_web/{posts[ii]}/{image_filename}", "r") as image_file:
            images = [jj.replace("\n", "") for jj in image_file.readlines()]

        n_images = len(images)

        with open(f"blog/imgs_web/{posts[ii]}/{caption_filename}", "r") as caption_file:
            captions = [jj.replace("\n", "") for jj in caption_file.readlines()]

        n_captions = len(captions)   

        assert n_images == n_captions, f"n_images needs to equal n_captions, but {n_images=} and {n_captions=} for {ii=}, post={posts[ii]}"

        with open(f"blog/content/{content_filename}", "r") as content_file:
            content = [jj.replace("\n", "") for jj in content_file.readlines()]

        content = "\n".join(content)

        if ii%2 + 1 == 1:
            color_selector_string = ''
        else:
            color_selector_string = 'u-palette-5-light-2'

        if ii <= 2:
            recentblog_file.write(make_post_title_section(ii, this_title, this_date, this_author, color_selector_string))
            recentblog_file.write(make_img_carousel(n_images, ii, posts, images, captions))
            recentblog_file.write(make_content(content, ii) + "\n")

        for ll in range(n_keywords):
            current_blog_keyword = keywords[ll]
            if current_blog_keyword in this_keywords:
                if n_post_per_keyword[ll]%2 + 1 == 1:
                    color_selector_string = ''
                else:
                    color_selector_string = 'u-palette-5-light-2'

                keyword_blog_pages[ll].write(make_post_title_section(ii, this_title, this_date, this_author, color_selector_string))
                keyword_blog_pages[ll].write(make_img_carousel(n_images, ii, posts, images, captions))
                keyword_blog_pages[ll].write(make_content(content, ii) + "\n")
                n_post_per_keyword[ll] += 1

    recentblog_file.write(blog_footer + "\n")


for ii, keyword in enumerate(keywords):
    keyword_blog_pages[ii].write(blog_footer + "\n")
    keyword_blog_pages[ii].close()


print("************************************************")
print("************************************************")
print("************************************************")
print("Blog pages have been successfully made!")
print("The following pages have been created: ")

for ii in range(n_keywords):
    print(f"{keywords[ii]}.html -- {n_post_per_keyword[ii]} posts")
print("************************************************")
print("************************************************")
print("************************************************")
