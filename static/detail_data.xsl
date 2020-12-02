<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">

<xsl:for-each select="tool">

<div class="container">
    <h5>Tool: <xsl:value-of select="name"/></h5>

    <h5>Url: <a href="https://www.youtube.com/" target="_blank">YouTube</a></h5>
    <h5>Price: <xsl:value-of select="free"/> </h5>
    <h5>Web based: <xsl:value-of select="web_based"/> </h5>
    <h5>Added on: <xsl:value-of select="added_on"/> </h5>
    <h5>ID: <xsl:value-of select="@temp_id"/> </h5>
</div>

</xsl:for-each>

</xsl:template>
</xsl:stylesheet>



