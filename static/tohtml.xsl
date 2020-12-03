<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">

        
<h2>Search and Recommendations</h2>
  <p>Las asta asa ca poate vrem sa scriem ceva AICI :)))</p>  
  <input class="form-control" id="myInput" type="text" placeholder="Search.."/>
  <br/> 

  <table class="table table-striped table-dark">
    <thead class="thead-dark">
      <tr>
        <th>Logo</th>
        <th>Name</th>
        <th>Url to toptools4learning</th>
        <th>Category</th>
        <th>Web based / Desktop</th>
        <th>Learning / teaching specific </th>
        <th>Free</th>
        <th>Added on</th>
      </tr>
    </thead>
  <xsl:for-each select="tools/tool">
    <tbody id="myTable">
      <tr>
        <td>
          <img style="width: 55px;">  
              <xsl:attribute name="src"><xsl:value-of select="image_logo"/></xsl:attribute>
              
          </img>
        </td>
        <td>
          <a>  
              <xsl:attribute name="href">/tools/id=<xsl:value-of select="@temp_id"/></xsl:attribute>
              <xsl:value-of select="name"/>
          </a>
        </td>

        <td> 

          <a>  
              <xsl:attribute name="href">
                <xsl:value-of select="url"/>
              </xsl:attribute>
              <xsl:value-of select="url"/>
          </a> 

        </td>

        <td><xsl:value-of select="category"/></td>

        <td><xsl:value-of select="web_based"/></td>


        <td>

          <xsl:if test="type='learning'">
            <p style="color:green"> 
              <xsl:value-of select="type"/> 
            </p>
          </xsl:if>

          <xsl:if test="type='teaching'">
            <p style="color:yellow"> 
              <xsl:value-of select="type"/>
            </p>
          </xsl:if>

        </td>


        <td><xsl:value-of select="free"/></td>

        <td><xsl:value-of select="added_on"/></td>

      </tr>
    </tbody>
  </xsl:for-each>
  </table>




</xsl:template>

</xsl:stylesheet>