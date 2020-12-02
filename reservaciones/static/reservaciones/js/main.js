let cont = 2
var str = ' '
for (var i=0; i < materias.length; i++){
    str += '<option value="'+materias[i]+'">'+materias[i]+'</option>'; 
}
let miLista = document.getElementById("lista1")
miLista.innerHTML = str

 function agregar(){

    if(cont <= 10){
        if(document.getElementById("materia"+cont)){
            cont = cont + 1
            agregar()
        }
        else {
            const inputList = document.getElementById("input-materias");
            const element = document.createElement("div");
            element.innerHTML = `
                <div class="form-row">
                    <div class="form-group col-md-12">
                        <label class="label-input d-block" for="materia${cont}">Materia ${cont} </label>
                        <input type="text" list="lista${cont}"class="form-control d-inline" name="materia${cont}" id="materia${cont}" style="width: 80%;" required>
                        <input type="button" value="X" name="removerBtn" class="btn btn-danger d-inline" style="width: 18%; height: 39px; ">
                        <datalist id="lista${cont}">            
                        </datalist>
                    </div>
                </div>
            `;
            inputList.appendChild(element);
            agregarDataList(cont);
            cont = cont + 1;
        }
    }
}


function agregarDataList(n) {
    let miLista = document.getElementById("lista"+n)
    miLista.innerHTML = str
}

function remover(element){
    if(element.name == "removerBtn"){
        element.parent
    }
}

document.getElementById("input-materias").addEventListener('click', function(e){
    if(e.target.name == "removerBtn"){
        e.target.parentElement.parentElement.parentElement.remove();
        cont = cont - 1
    }
});