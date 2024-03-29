# -*- coding: utf-8 -*-
from plone import api


def get_plantilles():
    """
    Declaració de les pàgines que es faràn servir com plantilles
    """
    portal = api.portal.get()
    absolute_url = portal.absolute_url()
    example_img_url = absolute_url + '/portal_skins/robtheme_images'

    plantilles = []
    titol = u"Rob Theme - Acordió"
    resum = u""
    cos = u"""
<div class="accordion" id="accordion1">
    <div class="accordion-group">
        <div class="accordion-heading"><a class="accordion-toggle fright collapsed" href="#collapse1" data-toggle="collapse" data-parent="#accordion1"> Collapsible Item #1 </a></div>
        <div class="accordion-body collapse" id="collapse1">
            <div class="accordion-inner">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce volutpat ac neque hendrerit varius. Etiam a viverra dolor. Duis vitae ex sed tortor elementum egestas. Proin efficitur lacus ac porttitor condimentum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus velit magna, accumsan id arcu quis, laoreet maximus est. Nullam suscipit augue eget posuere convallis. Morbi cursus sagittis nisl at varius. Vestibulum lacinia sem consectetur, accumsan est et, feugiat urna. Vivamus sit amet eros a diam sodales vestibulum.</div>
        </div>
    </div>
</div>
<div class="accordion" id="accordion2">
    <div class="accordion-group">
        <div class="accordion-heading"><a class="accordion-toggle fright collapsed" href="#collapse2" data-toggle="collapse" data-parent="#accordion2"> Collapsible Item #2 </a></div>
        <div class="accordion-body collapse" id="collapse2">
            <div class="accordion-inner">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce volutpat ac neque hendrerit varius. Etiam a viverra dolor. Duis vitae ex sed tortor elementum egestas. Proin efficitur lacus ac porttitor condimentum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus velit magna, accumsan id arcu quis, laoreet maximus est. Nullam suscipit augue eget posuere convallis. Morbi cursus sagittis nisl at varius. Vestibulum lacinia sem consectetur, accumsan est et, feugiat urna. Vivamus sit amet eros a diam sodales vestibulum.</div>
        </div>
    </div>
</div>
<div class="accordion" id="accordion3">
    <div class="accordion-group">
        <div class="accordion-heading"><a class="accordion-toggle fright collapsed" href="#collapse3" data-toggle="collapse" data-parent="#accordion3"> Collapsible Item #3 </a></div>
        <div class="accordion-body collapse" id="collapse3">
            <div class="accordion-inner">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce volutpat ac neque hendrerit varius. Etiam a viverra dolor. Duis vitae ex sed tortor elementum egestas. Proin efficitur lacus ac porttitor condimentum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus velit magna, accumsan id arcu quis, laoreet maximus est. Nullam suscipit augue eget posuere convallis. Morbi cursus sagittis nisl at varius. Vestibulum lacinia sem consectetur, accumsan est et, feugiat urna. Vivamus sit amet eros a diam sodales vestibulum.</div>
        </div>
    </div>
</div>
<p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Bàner gris amb icona Info"
    resum = u""
    cos = u"""
            <a class="link-banner-minimal" href="../" data-linktype="internal">
            <span class="fa fa-info-circle fa-2x"></span> LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.
        </a>
       <p>&nbsp;</p>
     """

    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Bàner blau amb icona Info"
    resum = u""
    cos = u"""
        <a class="link-banner-minimal-blue" href="../" data-linktype="internal">
            <span class="fa fa-info-circle fa-2x"></span> LOREM IPSUM - Lorem ipsum dolor sit amet consectetur adipiscing elit, eget eros facilisis risus dapibus ante nunc, accumsan libero odio mi porttitor egestas.
        </a>
       <p>&nbsp;</p>
    """

    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Bàner blau"
    resum = u""
    cos = u"""
        <a class="link-bannerblau" href="../">
            <span class="btntitolblau">Títol del banner</span>
            <br />
            <span class="btnsubtitolblau">Text descriptiu del banner</span>
          </a>
          <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Bàner gris"
    resum = u""
    cos = u"""
         <a class="link-banner" href="../">
            <span class="btntitol">Títol del banner</span>
            <br />
            <span class="btnsubtitol">Text descriptiu del banner</span>
          </a>
          <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Bàner vermell danger"
    resum = u""
    cos = u"""
          <a class="link-bannerdanger" href="../">
            <span class="btntitoldanger">Títol del banner</span>
            <br />
            <span class="btnsubtitoldanger">Text descriptiu del banner</span>
          </a>
        <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Bàner groc warning"
    resum = u""
    cos = u"""
          <a class="link-bannerwarning" href="../">
            <span class="btntitolwarning">Títol del banner</span>
            <br />
            <span class="btnsubtitolwarning">Text descriptiu del banner</span>
          </a>
          <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Bàner verd success"
    resum = u""
    cos = u"""
          <a class="link-bannersuccess" href="../">
            <span class="btntitolsuccess">Títol del banner</span>
            <br />
            <span class="btnsubtitolsuccess">Text descriptiu del banner</span>
          </a>
          <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Bàner amb imatge de fons"
    resum = u""
    cos = u"""
          <a class="link-bannerimg" href="../">
            <img alt="" src="capcalera.jpg" />
            <span class="btntitol">Títol del banner</span>
            <br />
            <span class="btnsubtitol">Text descriptiu del banner</span>
          </a>
          <p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Llista amb subllista"
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

    titol = u"Rob Theme - Destacat amb dades numèriques"
    resum = u""
    cos = u"""
<h2 class="titling-line">Lorem ipsum</h2>
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

    titol = u"Rob Theme - Caixa amb llista - fons gris"
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
                <span class="far fa-file-pdf"> </span> Contrary to popular belief, Lorem Ipsum is not simply random text.
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

    titol = u"Rob Theme - Caixa amb llista - fons verd"
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
                <span class="far fa-file-pdf"> </span> Contrary to popular belief, Lorem Ipsum is not simply random text.
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

    titol = u"Rob Theme - Graella d'imatges amb enllaços"
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
                             src="{0}/example-owl.jpeg" />
                    </a>
                </div>
                <div class="span2 gellery-bottom">
                    <a href="https://www.upc.edu" target="_blank" title="lorem">
                        <img alt="" class="logo" height="90" title="lorem" width="140"
                             src="{0}/example-owl.jpeg" />
                    </a>
                </div>
                <div class="span2 gellery-bottom">
                    <a href="https://www.upc.edu" target="_blank" title="lorem">
                        <img alt="" class="logo" height="90" title="lorem" width="140"
                             src="{0}/example-owl.jpeg" />
                    </a>
                </div>
                <div class="span2 gellery-bottom">
                    <a href="https://www.upc.edu" target="_blank" title="lorem">
                        <img alt="" class="logo" height="90" title="lorem" width="140"
                             src="{0}/example-owl.jpeg" />
                    </a>
                </div>
                <div class="span2 gellery-bottom">
                    <a href="https://www.upc.edu" target="_blank" title="lorem">
                        <img alt="" class="logo" height="90" title="lorem" width="140"
                             src="{0}/example-owl.jpeg" />
                    </a>
                </div>
                <div class="span2 gellery-bottom">
                    <a href="https://www.upc.edu" target="_blank" title="lorem">
                        <img alt="" class="logo" height="90" title="lorem" width="140"
                             src="{0}/example-owl.jpeg" />
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp;</p>
    """.format(example_img_url)
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Llistat opcions amb icones lletres - 2 col"
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
                <h2><a href="#">LOREM IPSUM</a></h2>
                <p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC.</p>
            </li>
            <li>
                <div class="lletra-cercle-a lletra-cercle color-carbassa"></div>
                <h2><a href="#">LOREM IPSUM</a></h2>
                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
            </li>
            <li>
                <div class="lletra-cercle-a lletra-cercle color-verd"></div>
                <h2><a class="internal-link" href="#" target="_self" title="">LOREM IPSUM</a></h2>
                <p style="text-align: justify; ">There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.</p>
            </li>
            <li>
                <div class="lletra-cercle-u lletra-cercle color-morat"></div>
                <h2><a href="#">LOREM IPSUM</a></h2>
                <p>The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested.</p>
            </li>
            <li>
                <div class="lletra-cercle-c lletra-cercle color-blau"></div>
                <h2><a href="#" target="_blank">LOREM IPSUM</a></h2>
                <p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.</p>
            </li>
            <li>
                <div class="lletra-cercle-m lletra-cercle color-lila"></div>
                <h2><a href="#" target="_blank">LOREM IPSUM</a></h2>
                <p>The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.</p>
            </li>
        </ul>
    </div>
    <div class="span6">
        <ul class="list-sections">
            <li>
                <div class="lletra-cercle-d lletra-cercle color-verd"></div>
                <h2><a class="external-link" href="#" target="_blank">LOREM IPSUM</a></h2>
                <p>The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested.</p>
            </li>
            <li>
                <div class="lletra-cercle-i lletra-cercle color-morat"></div>
                <h2><a href="#">LOREM IPSUM</a></h2>
                <p>Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>
            </li>
            <li>
                <div class="lletra-cercle-i lletra-cercle color-blau"></div>
                <h2><a href="#">LOREM IPSUM</a></h2>
                <p>If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.</p>
            </li>
            <li>
                <div class="lletra-cercle-q lletra-cercle color-carbassa"></div>
                <h2><a href="#">LOREM IPSUM</a></h2>
                <p>It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.</p>
            </li>
            <li>
                <div class="lletra-cercle-e lletra-cercle color-lila"></div>
                <h2><a href="#">LOREM IPSUM</a></h2>
                <p>Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text.</p>
            </li>
            <li>
                <div class="lletra-cercle-a lletra-cercle color-verd"></div>
                <h2><a class="internal-link" href="#" target="_self">LOREM IPSUM</a></h2>
                <p>The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.</p>
            </li>
        </ul>
    </div>
</div>
<p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Conjunt imatge amb llista opcions - 3 col"
    resum = u""
    cos = u"""
<div class="row-fluid">
    <div class="span4">
        <div class="thumbnails">
            <a href="#">
                <img alt="" class="image-inline" title="" width="100%"
                     src="{0}/example-fox.jpeg" />
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
            <a href="#">
                <img alt="" class="image-inline" title="" width="100%"
                     src="{0}/example-penguin.jpeg" />
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
            <a href="#">
                <img alt="" class="image-inline" title="" width="100%"
                     src="{0}/example-artic-fox.jpeg" />
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
    """.format(example_img_url)
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Destacat amb imatge"
    resum = u""
    cos = u"""
<div class="destacat destacat-dreta" style="height: 444px;">
    <div class="destacat-contingut">
        <p>It is a <strong>long established</strong> fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use <strong>Lorem Ipsum</strong> as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy.</p>
        <h2 class="h3" style="text-align: right; "><a href="#"><strong><br />Lorem Ipsum UPC</strong></a></h2>
        <p style="text-align: right; "><strong> Lorem Ipsum Universitat politècnica Catalunya </strong></p>
    </div>
    <div class="destacat-imatge">
        <img alt="" class="image-inline" title="" width="100%"
             src="{0}/example-penguin.jpeg" /></div>
</div>
<p>&nbsp;</p>
    """.format(example_img_url)
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Frase destacada"
    resum = u""
    cos = u"""
<div>
    <div class="box">
        <h2 class="align-center">
            <span class="fa fa-quote-left"></span>
            Lorem Ipsum is simply dummy text of the printing and typesetting industry
            <span class="fa fa-quote-right"></span>
        </h2>
        <p><span>Lorem Ipsum</span></p>
    </div>
</div>
<p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    titol = u"Rob Theme - Columna de suport"
    resum = u""
    cos = u"""
<h2>Titular del bloc de text</h2>
<div class="row-fluid">
    <div class="span8">
        <div class="well">
            <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Duis tellus. Donec ante dolor, iaculis nec, gravida ac, cursus in, eros. Mauris vestibulum, felis et egestas ullamcorper, <a href="javascript: ;">purus nibh vehicula sem</a>, eu egestas ante nisl non justo. Fusce tincidunt, lorem nec dapibus consectetuer, leo orci mollis ipsum, eget suscipit eros purus in ante.</p>
        </div>
        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
        <p>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled.</p>
    </div>
    <div class="span4">
        <div class="box pull-right">
            <h3>Enllaços relacionats</h3>
            <ul class="list list-links">
                <li><a href="#">JDuis tellus</a></li>
                <li><a href="#">Maecenas elit orci</a></li>
                <li><a href="#">At ipsum vitae est lacinia tincidunt</a></li>
            </ul>
            <h3>Bàners</h3>
            <p>
                <a class="link-banner-minimal" href="#" data-linktype="internal">
                    <img alt="" src="capcalera.jpg" title="etsab" />
                    <span>Bàner mostra</span>
                </a>
            </p>
            <p><a class="link-banner-minimal" href="#" data-linktype="internal">Bàner mostra</a></p>
            <p><a class="link-banner-minimal-blue" href="#" data-linktype="internal">Bàner mostra </a></p>
            <p>&nbsp;</p>
        </div>
    </div>
</div>
<p>&nbsp;</p>
    """
    plantilles.append({'titol': titol, 'resum': resum, 'cos': cos})

    return plantilles
