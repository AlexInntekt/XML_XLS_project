
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">

    <h2>Here is your table</h2>
    <table border="1">
      <tr bgcolor="#9acd32">
        <th>Name</th>
        <th>Url</th>
        <th>Category</th>
      </tr>
      <xsl:for-each select="tools/tool">
        <tr>
          <td><xsl:value-of select="name"/></td>
          <td><xsl:value-of select="url"/></td>
          <td><xsl:value-of select="category"/></td>
        </tr>
      </xsl:for-each>
    </table>

</xsl:template>

</xsl:stylesheet>