<html>
    <body>
    <script type="text/javascript">
    
    var w = 500;
    var h = 100;
    var barPadding = 1;
    
    var dataset = [ 50, 100 ];
    
    //Create SVG element
    var svg = d3.select("body")
                .append("svg")
                .attr("width", w)
                .attr("height", h);

    svg.selectAll("rect")
       .data(dataset)
       .enter()
       .append("rect")
       .attr("x", function(d, i) {
            return i
       })
       .attr("y", function(d) {
            return d
       })
       .attr("width", 50)
       .attr("height", function(d) {
            return d;
       });
    </script>
    </body>
</html>

