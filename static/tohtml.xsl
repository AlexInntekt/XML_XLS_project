<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">

<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"/>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
  
<div class="container">
  <h2>Search and Recommendations</h2>
  <p>Las asta asa ca poate vrem sa scriem ceva AICI :)))</p>  
  <input class="form-control" id="myInput" type="text" placeholder="Search.."/>
  <br/>          
  <table class="table table-striped table-dark">
    <thead class="thead-dark">
      <tr>
        <th>Name</th>
        <th>Url to toptools4learning</th>
        <th>Category</th>
        <th>Web based / Desktop</th>
        <th>Learning / teaching specific </th>
        <th>Free</th>
      </tr>
    </thead>
  <xsl:for-each select="tools/tool">
    <tbody id="myTable">
      <tr>
        <td>
          <a>  
              <xsl:attribute name="href">
                tools/id=<xsl:value-of select="@temp_id"/>
              </xsl:attribute>
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
      </tr>
    </tbody>
  </xsl:for-each>
  </table>
</div>
<script>
  $(document).ready(function(){
    $("#myInput").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#myTable tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });
  </script>
</body>
</html>



</xsl:template>

</xsl:stylesheet>