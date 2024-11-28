"""<!DOCTYPE html>
<html>
<title>Scribe</title>
<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<style>

    *{
        padding: 0;
        margin: 0;
    }

    .title{
        text-align: center;
    }

    .content{
        padding: 10px;
    }

    .row{
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        margin-top: 10px;
        background-color: #9111;
    }

    .centered{
        text-align: center;
    }

</style>
</head>
<body>

    <div class="content">

        <h2 class="title">Test Report</h2>

        <h3 class="centered">{{page_date}}</h3>
        <!-- <h4 class="centered">{{page_name}}</h4> -->

        <div class="list container">

            <table class="table">
                <thead>
                    <tr>
                    <th scope="col">{{column_1}}</th>
                    <th scope="col">{{column_2}}</th>
                    <th scope="col">{{column_3}}</th>
                    <th scope="col">actual result
                        <select id="myDropdown" onchange="filterElements(this)">
                            <option value="all">All</option>
                            <option value="success">Success</option>
                            <option value="failure">Failure</option>
                        </select>
                    </th>
                    </tr>
                </thead>
                <tbody>
                    {{nextrow}}
                </tbody>
            </table>

        </div>

    
    </div>
    <script type="text/javascript">
        function filterElements(elm){

            var elements = document.querySelectorAll('tr');
            elements.forEach(element => {
                innerElement = element.querySelectorAll("td");
                innerElement.forEach(column => {
                    if(column.textContent.includes(elm.value) || elm.value==null || elm.value=="all"){
                        element.hidden = false;
                    } else{
                        element.hidden = true;
                    }
                });
            });
        }
        function dynamicIndex(elm){

            let index = 1;

            var elements = document.querySelectorAll('th');

            for (i=4; i<elements.length; i++){
                elements[i].innerHTML = index++;
            };
        }
        dynamicIndex();
    </script>
</body>

</html>
"""