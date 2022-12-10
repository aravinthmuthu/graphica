fetch("http://0.0.0.0:8080/denis.json")
.then((response) => response.json())
.then((data) => {
    
    Tree(data, {
        div_id: "#d3_elem",
        label: d => d.name,
        title: (d, n) => `${n.ancestors().reverse().map(d => d.data.name).join(".")}`, // hover text
        width: 1152,
        height: 1152,
        margin: 100
    });

});
