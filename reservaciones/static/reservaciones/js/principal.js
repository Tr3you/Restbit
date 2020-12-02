let nEntrante = 2
let nFuerte = 2
let nPostre = 2
var strEntrantes= `
<option value="PE1">Crema de Boletus y Trufa</option>
<option value="PE2">Croquetas de Jamón Ibérico</option>
<option value="PE3">Mini Tatín de Manzana y Foie</option>
<option value="PE4">Espiral de Langostino y Kimchi</option>
<option value="PE5">Piruleta de Queso de Cabra</option>
`;
var strFuertes = `
<option value="PF1">Sopa de Mariscos</option>
<option value="PF2">Albondigas de Pavo con Crema de Queso Parmesano</option>
<option value="PF3">Pollo con Salsa Danna</option>
<option value="PF4">Lomo de cerdo</option>
<option value="PF5">Albóndiga en Salsa de Tres Chiles</option>
`;
var strPostres = `
<option value="PP1">Coulant de chocolate</option>
<option value="PP2">Migajón de palo cortado</option>
<option value="PP3">Tarta de yogurt y frutos del bosque</option>
<option value="PP4">Cheesecake de dulce de leche</option>
<option value="PP5">Tiramisu</option>
`;

function agregarEntrante(){
    if(document.getElementById("entrante"+nEntrante)){
        nEntrante = nEntrante + 1
        agregarEntrante()
    }
    else{
        const inputList = document.getElementById("input-entrantes");
        const element = document.createElement("div");
        element.innerHTML = `
            <div class="form-row">
                <div class="form-group col-md-12">
                    <label class="label-input d-block" for="entrante${nEntrante}">Entrante ${nEntrante} </label>
                    <input type="text" list="entrantesList${nEntrante}"class="form-control d-inline" name="entrante${nEntrante}" id="entrante${nEntrante}" style="width: 80%;" required>
                    <input type="button" value="X" name="removerBtn" class="btn btn-danger d-inline" style="width: 18%; height: 39px; ">
                    <datalist id="entrantesList${nEntrante}">            
                    </datalist>
                </div>
            </div>
                `;
        inputList.appendChild(element);
        agregarDataListEntrante(nEntrante);
        nEntrante = nEntrante + 1;
    }
}

function agregarDataListEntrante(n){
    let miLista = document.getElementById("entrantesList"+n)
    miLista.innerHTML = strEntrantes
}


document.getElementById("input-entrantes").addEventListener('click', function(e){
    if(e.target.name == "removerBtn"){
        e.target.parentElement.parentElement.parentElement.remove();
        nEntrante = nEntrante - 1
    }
});

function agregarFuerte(){
    if(document.getElementById("fuerte"+nFuerte)){
        nFuerte = nFuerte + 1
        agregarFuerte()
    }
    else{
        const inputList = document.getElementById("input-fuertes");
        const element = document.createElement("div");
        element.innerHTML = `
            <div class="form-row">
                <div class="form-group col-md-12">
                    <label class="label-input d-block" for="fuerte${nFuerte}">Plato Fuerte ${nFuerte} </label>
                    <input type="text" list="fuertesList${nFuerte}"class="form-control d-inline" name="fuerte${nFuerte}" id="fuerte${nFuerte}" style="width: 80%;" required>
                    <input type="button" value="X" name="removerBtn" class="btn btn-danger d-inline" style="width: 18%; height: 39px; ">
                    <datalist id="fuertesList${nFuerte}">            
                    </datalist>
                </div>
            </div>
                `;
        inputList.appendChild(element);
        agregarDataListFuerte(nFuerte);
        nFuerte = nFuerte + 1;
    }
}

function agregarDataListFuerte(n){
    let miLista = document.getElementById("fuertesList"+n)
    miLista.innerHTML = strFuertes
}


document.getElementById("input-fuertes").addEventListener('click', function(e){
    if(e.target.name == "removerBtn"){
        e.target.parentElement.parentElement.parentElement.remove();
        nFuerte = nFuerte - 1
    }
});

function agregarPostre(){
    if(document.getElementById("postre"+nPostre)){
        nPostre = nPostre + 1
        agregarPostre()
    }
    else{
        const inputList = document.getElementById("input-postres");
        const element = document.createElement("div");
        element.innerHTML = `
            <div class="form-row">
                <div class="form-group col-md-12">
                    <label class="label-input d-block" for="postre${nPostre}">Postre ${nPostre} </label>
                    <input type="text" list="postresList${nPostre}"class="form-control d-inline" name="postre${nPostre}" id="postre${nPostre}" style="width: 80%;" required>
                    <input type="button" value="X" name="removerBtn" class="btn btn-danger d-inline" style="width: 18%; height: 39px; ">
                    <datalist id="postresList${nPostre}">            
                    </datalist>
                </div>
            </div>
                `;
        inputList.appendChild(element);
        agregarDataListPostre(nPostre);
        nPostre = nPostre + 1;
    }
}

function agregarDataListPostre(n){
    let miLista = document.getElementById("postresList"+n)
    miLista.innerHTML = strPostres
}


document.getElementById("input-postres").addEventListener('click', function(e){
    if(e.target.name == "removerBtn"){
        e.target.parentElement.parentElement.parentElement.remove();
        nPostre = nPostre - 1
    }
});