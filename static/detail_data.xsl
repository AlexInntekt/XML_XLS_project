<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">

<xsl:for-each select="tool">




<div class="container-fluid">
    <div class="media">

        <img class="mr-3" style="width: 300px;">  
              <xsl:attribute name="src"><xsl:value-of select="image_logo"/></xsl:attribute>
        </img>

        <div class="media-body">
            <br/>
            <hr/>
            <h5 class="mt-0">Name: <xsl:value-of select="name"/></h5>
            <h5 class="mt-0">Description</h5>
          	<p><xsl:value-of select="description"/></p>
     	</div>
    </div>
</div>
<br/>
<br/>

<div class="container">
    <h5>Tool: <xsl:value-of select="name"/> </h5>

    <h5>
        <a>  
            <xsl:attribute name="href"><xsl:value-of select="url"/></xsl:attribute>
            <xsl:value-of select="name"/>
        </a>
    </h5>

    <h5>Price: <xsl:value-of select="free"/> </h5>
    <h5>Web based: <xsl:value-of select="web_based"/> </h5>
    <h5>Proper for engineering: <xsl:value-of select="engineering"/> </h5>
    <h5>Added on: <xsl:value-of select="added_on"/> </h5>
    <h5>ID: <xsl:value-of select="@temp_id"/> </h5>
    <h5>Rank: <xsl:value-of select="position"/> </h5>
</div>

</xsl:for-each>

</xsl:template>
</xsl:stylesheet>



