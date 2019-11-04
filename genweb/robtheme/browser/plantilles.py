# -*- coding: utf-8 -*-


def get_plantilles():
    """
    Declaració de les pàgines que es faràn servir com plantilles
    """
    plantilles = []
    titol = u"Rob Theme - Acordió"
    resum = u""
    cos = u"""
<div class="accordion" id="accordion2">
    <div class="accordion-group">
        <div class="accordion-heading">
            <a class="accordion-toggle collapsed fright" href="#collapseOne" data-toggle="collapse" data-parent="#accordion2"> Collapsible Group Item #1 </a>
        </div>
        <div class="accordion-body collapse" id="collapseOne">
            <div class="accordion-inner">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce volutpat ac neque hendrerit varius. Etiam a viverra dolor. Duis vitae ex sed tortor elementum egestas. Proin efficitur lacus ac porttitor condimentum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus velit magna, accumsan id arcu quis, laoreet maximus est. Nullam suscipit augue eget posuere convallis. Morbi cursus sagittis nisl at varius. Vestibulum lacinia sem consectetur, accumsan est et, feugiat urna. Vivamus sit amet eros a diam sodales vestibulum.</div>
        </div>
    </div>
    <div class="accordion-group">
        <div class="accordion-heading">
            <a class="accordion-toggle collapsed fright" href="#collapseTwo" data-toggle="collapse" data-parent="#accordion2"> Collapsible Group Item #2 </a>
        </div>
        <div class="accordion-body collapse" id="collapseTwo">
            <div class="accordion-inner">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce volutpat ac neque hendrerit varius. Etiam a viverra dolor. Duis vitae ex sed tortor elementum egestas. Proin efficitur lacus ac porttitor condimentum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus velit magna, accumsan id arcu quis, laoreet maximus est. Nullam suscipit augue eget posuere convallis. Morbi cursus sagittis nisl at varius. Vestibulum lacinia sem consectetur, accumsan est et, feugiat urna. Vivamus sit amet eros a diam sodales vestibulum.</div>
        </div>
    </div>
    <div class="accordion-group">
        <div class="accordion-heading">
            <a class="accordion-toggle collapsed fright" href="#collapseThree" data-toggle="collapse" data-parent="#accordion2"> Collapsible Group Item #3 </a>
        </div>
        <div class="accordion-body collapse" id="collapseThree">
            <div class="accordion-inner">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce volutpat ac neque hendrerit varius. Etiam a viverra dolor. Duis vitae ex sed tortor elementum egestas. Proin efficitur lacus ac porttitor condimentum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus velit magna, accumsan id arcu quis, laoreet maximus est. Nullam suscipit augue eget posuere convallis. Morbi cursus sagittis nisl at varius. Vestibulum lacinia sem consectetur, accumsan est et, feugiat urna. Vivamus sit amet eros a diam sodales vestibulum.</div>
        </div>
    </div>
</div>
<p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Banner Text Link - Icona Info - GRIS"
    resum = u""
    cos = u"""
        <a class="link-banner-minimal" href="../" data-linktype="internal">
            <i class="fa fa-info-circle fa-2x"></i> LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.
        </a>
       <p>&nbsp;</p>
     """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Banner Text Link - Icona Arxiu - GRIS"
    resum = u""
    cos = u"""
        <a class="link-banner-minimal" href="../" data-linktype="internal">
            <i class="fa fa-archive fa-2x"></i> LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.
        </a>
        <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Banner Text Link - Icona Info - BLAU"
    resum = u""
    cos = u"""
        <a class="link-banner-minimal-blue" href="../" data-linktype="internal">
            <i class="fa fa-info-circle fa-2x"></i> LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.
        </a>
       <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Banner Text Link - Icona Arxiu - BLAU"
    resum = u""
    cos = u"""
        <a class="link-banner-minimal-blue" href="../" data-linktype="internal">
            <i class="fa fa-archive fa-2x"></i> LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.
        </a>
       <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Banner Text No Link - Icona Info - GRIS"
    resum = u""
    cos = u"""
        <a class="link-banner-minimal-nolink" data-linktype="internal">
            <i class="fa fa-info-circle fa-2x"></i> LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.
        </a>
        <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Banner Text No Link - Icona Arxiu - GRIS"
    resum = u""
    cos = u"""
        <a class="link-banner-minimal-nolink" data-linktype="internal">
            <i class="fa fa-archive fa-2x"></i> LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.
        </a>
        <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Banner Text No Link - Icona Info - BLAU"
    resum = u""
    cos = u"""
        <a class="link-banner-minimal-nolink-blue" data-linktype="internal">
            <i class="fa fa-info-circle fa-2x"></i> LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.
        </a>
        <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Banner Text No Link - Icona Arxiu - BLAU"
    resum = u""
    cos = u"""
        <a class="link-banner-minimal-nolink-blue" data-linktype="internal">
            <i class="fa fa-archive fa-2x"></i> LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.
        </a>
        <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Banner Text Link - Imatge"
    resum = u""
    cos = u"""
        <a class="link-banner-minimal" href="../" data-linktype="internal">
            <img alt="" src="../capcalera.jpg" />
            <span>LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.</span>
        </a>
       <p>&nbsp;</p>
     """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Banner Text No Link - Imatge"
    resum = u""
    cos = u"""
        <a class="link-banner-minimal-nolink" data-linktype="internal">
            <img alt="" src="../capcalera.jpg" />
            <span>LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.</span>
        </a>
        <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Botó Destacat BLAU"
    resum = u""
    cos = u"""
        <a class="link-bannerblau" href="../">
            <span class="btntitolblau">Lorem Ipsum</span>
            <br />
            <span class="btnsubtitolblau">It is a long established fact that a reader will ...</span>
          </a>
          <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Botó Destacat GRIS"
    resum = u""
    cos = u"""
         <a class="link-banner" href="../">
            <span class="btntitol">Lorem Ipsum</span>
            <br />
            <span class="btnsubtitol">It is a long established fact that a reader will ...</span>
          </a>
          <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Botó Destacat DANGER"
    resum = u""
    cos = u"""
          <a class="link-bannerdanger" href="../">
            <span class="btntitoldanger">Lorem Ipsum</span>
            <br />
            <span class="btnsubtitoldanger">It is a long established fact that a reader will ...</span>
          </a>
        <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Botó Destacat WARNING"
    resum = u""
    cos = u"""
          <a class="link-bannerwarning" href="../">
            <span class="btntitolwarning">Lorem Ipsum</span>
            <br />
            <span class="btnsubtitolwarning">It is a long established fact that a reader will ...</span>
          </a>
          <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Botó Destacat SUCCESS"
    resum = u""
    cos = u"""
          <a class="link-bannersuccess" href="../">
            <span class="btntitolsuccess">Lorem Ipsum</span>
            <br />
            <span class="btnsubtitolsuccess">It is a long established fact that a reader will ...</span>
          </a>
          <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Llista amb subllista UPC"
    resum = u""
    cos = u"""
<ul class="list-links-upc">
    <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
    <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
    <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
    <ul class="llistaesquerra">
        <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
        <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
        <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
    </ul>
</ul>
<p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Dades numèriques"
    resum = u""
    cos = u"""
<h2 class="titling-line">LOREM IPSUM</h2>
<div class="well">
    <ul class="list-numeral">
        <li>
            <strong>11</strong> What is Lorem Ipsum?
        </li>
        <li>
            <strong>400</strong> Where does it come from?
        </li>
        <li>
            <strong>60</strong> Why do we use it?
        </li>
        <li>
            <strong>91%</strong> Where can I get some?
        </li>
        <li>
            <strong>1360</strong> Neque porro quisquam
        </li>
        <li>
            <strong>6</strong> adipisci velit
        </li>
    </ul>
</div>
<p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Caixa amb llista - UPC GRIS"
    resum = u""
    cos = u"""
    <div class="boxbg-gray">
        <h3>Lorem Ipsum</h3>
        <ul class="list-links-upc">
            <li>
                Contrary to popular belief, Lorem Ipsum is not simply random text.
                <strong>Lorem Ipsum.</strong>
            </li>
            <li>
                Contrary to popular belief, Lorem Ipsum is not simply random text.
                <strong>Lorem Ipsum.</strong>
            </li>
            <li>
                <i class="far fa-file-pdf"> </i> Contrary to popular belief, Lorem Ipsum is not simply random text.
                <strong>
                <a href="../">Lorem Ipsum!</a>
              </strong>
            </li>
        </ul>
        <p>The
            <strong>lorem ipcum</strong> there are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour.
        </p>
    </div>
    <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Caixa amb llista - VERD"
    resum = u""
    cos = u"""
    <div class="boxbg-green">
        <h3>Lorem Ipsum</h3>
        <ul class="list-links-upc">
            <li>
                Contrary to popular belief, Lorem Ipsum is not simply random text.
                <strong>Lorem Ipsum.</strong>
            </li>
            <li>
                Contrary to popular belief, Lorem Ipsum is not simply random text.
                <strong>Lorem Ipsum.</strong>
            </li>
            <li>
                <i class="far fa-file-pdf"> </i> Contrary to popular belief, Lorem Ipsum is not simply random text.
                <strong>
                <a href="../">Lorem Ipsum!</a>
              </strong>
            </li>
        </ul>
        <p>The
            <strong>lorem ipcum</strong> there are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour.
        </p>
    </div>
   <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Graella imatges"
    resum = u""
    cos = u"""
<h2 class="titling-line">Lorem Ipsum</h2>
<div id="gallery-grid">
    <div class="row-fluid">
        <div class="span12">
            <div class="row-fluid gallery-logos">
                <div class="span2 gellery-bottom">
                    <a href="https://www.upc.edu" target="_blank" title="lorem">
                        <img alt="" class="logo" height="90" title="lorem" width="140"
                             src="https://www.jqueryscript.net/images/Universal-Placeholder-Text-Lorem-Ipsum-Generator-getlorem.jpg" />
                    </a>
                </div>
                <div class="span2 gellery-bottom">
                    <a href="https://www.upc.edu" target="_blank" title="lorem">
                        <img alt="" class="logo" height="90" title="lorem" width="140"
                             src="https://www.jqueryscript.net/images/Universal-Placeholder-Text-Lorem-Ipsum-Generator-getlorem.jpg" />
                    </a>
                </div>
                <div class="span2 gellery-bottom">
                    <a href="https://www.upc.edu" target="_blank" title="lorem">
                        <img alt="" class="logo" height="90" title="lorem" width="140"
                             src="https://www.jqueryscript.net/images/Universal-Placeholder-Text-Lorem-Ipsum-Generator-getlorem.jpg" />
                    </a>
                </div>
                <div class="span2 gellery-bottom">
                    <a href="https://www.upc.edu" target="_blank" title="lorem">
                        <img alt="" class="logo" height="90" title="lorem" width="140"
                             src="https://www.jqueryscript.net/images/Universal-Placeholder-Text-Lorem-Ipsum-Generator-getlorem.jpg" />
                    </a>
                </div>
                <div class="span2 gellery-bottom">
                    <a href="https://www.upc.edu" target="_blank" title="lorem">
                        <img alt="" class="logo" height="90" title="lorem" width="140"
                             src="https://www.jqueryscript.net/images/Universal-Placeholder-Text-Lorem-Ipsum-Generator-getlorem.jpg" />
                    </a>
                </div>
                <div class="span2 gellery-bottom">
                    <a href="https://www.upc.edu" target="_blank" title="lorem">
                        <img alt="" class="logo" height="90" title="lorem" width="140"
                             src="https://www.jqueryscript.net/images/Universal-Placeholder-Text-Lorem-Ipsum-Generator-getlorem.jpg" />
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - llistat opcions- icones lletres - 2 cols"
    resum = u""
    cos = u"""
<div class="row-fluid">
    <h2>Lorem Ipsum</h2>
</div>
<div class="row-fluid">
    <div class="span6">
        <ul class="list-sections">
            <li>
                <div class="lletra-cercle-p lletra-cercle color-blau"></div>
                <h2><a href="upc">LOREM IPSUM</a></h2>
                <p class="hidden-phone">Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC.</p>
            </li>
            <li>
                <div class="lletra-cercle-a lletra-cercle color-carbassa"></div>
                <h2><a href="upc">LOREM IPSUM</a></h2>
                <p class="hidden-phone">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
            </li>
            <li>
                <div class="lletra-cercle-a lletra-cercle color-verd"></div>
                <h2><a class="internal-link" href="upc" target="_self" title="">LOREM IPSUM</a></h2>
                <p class="hidden-phone" style="text-align: justify; ">There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.</p>
            </li>
            <li>
                <div class="lletra-cercle-u lletra-cercle color-morat"></div>
                <h2><a href="upc">LOREM IPSUM</a></h2>
                <p class="hidden-phone">The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested.</p>
            </li>
            <li>
                <div class="lletra-cercle-c lletra-cercle color-blau"></div>
                <h2><a href="upc" target="_blank">LOREM IPSUM</a></h2>
                <p class="hidden-phone">There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.</p>
            </li>
            <li>
                <div class="lletra-cercle-m lletra-cercle color-lila"></div>
                <h2><a href="upc" target="_blank">LOREM IPSUM</a></h2>
                <p class="hidden-phone">The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.</p>
            </li>
        </ul>
    </div>
    <div class="span6">
        <ul class="list-sections">
            <li>
                <div class="lletra-cercle-d lletra-cercle color-verd"></div>
                <h2><a class="external-link" href="upc" target="_blank">LOREM IPSUM</a></h2>
                <p class="hidden-phone">The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested.</p>
            </li>
            <li>
                <div class="lletra-cercle-i lletra-cercle color-morat"></div>
                <h2><a href="upc">LOREM IPSUM</a></h2>
                <p class="hidden-phone">Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>
            </li>
            <li>
                <div class="lletra-cercle-i lletra-cercle color-blau"></div>
                <h2><a href="upc">LOREM IPSUM</a></h2>
                <p class="hidden-phone">If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.</p>
            </li>
            <li>
                <div class="lletra-cercle-q lletra-cercle color-carbassa"></div>
                <h2><a href="upc">LOREM IPSUM</a></h2>
                <p class="hidden-phone">It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.</p>
            </li>
            <li>
                <div class="lletra-cercle-e lletra-cercle color-lila"></div>
                <h2><a href="upc">LOREM IPSUM</a></h2>
                <p class="hidden-phone">Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text.</p>
            </li>
            <li>
                <div class="lletra-cercle-a lletra-cercle color-verd"></div>
                <h2><a class="internal-link" href="upc" target="_self">LOREM IPSUM</a></h2>
                <p class="hidden-phone">The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.</p>
            </li>
        </ul>
    </div>
</div>
<p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Conjunt Imatge amb llista opcions - 3 cols"
    resum = u""
    cos = u"""
<div class="row-fluid">
    <div class="span4">
        <div class="thumbnails">
            <a class="hidden-phone" href="#">
                <img alt="" class="image-inline" title="" width="100%"
                     src="https://www.jqueryscript.net/images/Universal-Placeholder-Text-Lorem-Ipsum-Generator-getlorem.jpg" />
            </a>
            <div class="caption">
                <h2 class="h224">Lorem Ipsum</h2>
                <ul class="list-links-upc">
                    <li><a class="internal-link" href="#" target="_self" title="">What is Lorem Ipsum?</a></li>
                    <li><a class="external-link" href="#" target="_blank" title="">Why do we use it?</a></li>
                    <li><a class="internal-link" href="#" target="_blank" title="">Where can I get some?</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="span4">
        <div class="thumbnails">
            <a class="hidden-phone" href="#">
                <img alt="" class="image-inline" title="" width="100%"
                     src="https://www.jqueryscript.net/images/Universal-Placeholder-Text-Lorem-Ipsum-Generator-getlorem.jpg" />
            </a>
            <div class="caption">
                <h2 class="h224">Lorem Ipsum</h2>
                <ul class="list-links-upc">
                    <li><a class="internal-link" href="#" target="_self" title="">What is Lorem Ipsum?</a></li>
                    <li><a class="external-link" href="#" target="_blank" title="">Why do we use it?</a></li>
                    <li><a class="internal-link" href="#" target="_blank" title="">Where can I get some?</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="span4">
        <div class="thumbnails">
            <a class="hidden-phone" href="#">
                <img alt="" class="image-inline" title="" width="100%"
                     src="https://www.jqueryscript.net/images/Universal-Placeholder-Text-Lorem-Ipsum-Generator-getlorem.jpg" />
            </a>
            <div class="caption">
                <h2 class="h224">Lorem Ipsum</h2>
                <ul class="list-links-upc">
                    <li><a class="internal-link" href="#" target="_self" title="">What is Lorem Ipsum?</a></li>
                    <li><a class="external-link" href="#" target="_blank" title="">Why do we use it?</a></li>
                    <li><a class="internal-link" href="#" target="_blank" title="">Where can I get some?</a></li>
                </ul>
            </div>
        </div>
    </div>
</div>
<p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Destacat amb imatge"
    resum = u""
    cos = u"""
<div class="destacat destacat-dreta hidden-phone" style="height: 444px;">
    <div class="destacat-contingut hidden-phone">
        <p>It is a <strong>long established</strong> fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use <strong>Lorem Ipsum</strong> as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy.</p>
        <h2 class="h3" style="text-align: right; "><a href="#"><strong><br />Lorem Ipsum UPC</strong></a></h2>
        <p style="text-align: right; "><strong> Lorem Ipsum Universitat politècnica Catalunya </strong></p>
    </div>
    <div class="destacat-imatge hidden-phone">
        <img alt="" class="image-inline" title="" width="100%"
             src="https://www.jqueryscript.net/images/Universal-Placeholder-Text-Lorem-Ipsum-Generator-getlorem.jpg" /></div>
</div>
<p></p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Frase destacada"
    resum = u""
    cos = u"""
<div class="hidden-phone">
    <div class="box">
        <h2 class="align-center">
            <i class="fa fa-quote-left"></i>
            Lorem Ipsum is simply dummy text of the printing and typesetting industry
            <i class="fa fa-quote-right"></i>
        </h2>
        <p><i>Lorem Ipsum</i></p>
    </div>
</div>
<p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    return plantilles
