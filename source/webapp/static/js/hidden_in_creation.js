type = document.getElementById("id_expert_type");   //Находим поле тип эксперта

sertification_child = document.getElementById("id_certification_status"); //Находим поле сертифицированности
sertification = sertification_child.parentNode;   //Находим блок сертифицированности по его полю

affiliation_child = document.getElementById("id_affiliation");    //Находим поле аффилированности
affiliation = affiliation_child.parentNode;       //Находим блок аффилированности по его полю

year_of_end_child = document.getElementById("id_year_of_end");    //Находим поле года окончания
year_of_end = year_of_end_child.parentNode;       //Находим блок года окончания по его полю

function hide(type) {       //Создаем функцию прятания полей, принимает тип эксперта
  if (type === "international expert" || type === "employer") {     //Если тип междунар эксперт или работодатель, то скрываем поля сертифицированности, аффилированности и года окончания
    sertification.hidden = true;
    affiliation.hidden = true;
    year_of_end.hidden = true;
  } else if (type === "sgk expert"){
    sertification.hidden = true;
    affiliation.hidden = false;
    year_of_end.hidden = true;
  } else if (type === "student"){
    sertification.hidden = true;
    affiliation.hidden = false;
    year_of_end.hidden = false;
  } else if(type === "academic expert"){
    sertification.hidden = false;
    affiliation.hidden = false;
    year_of_end.hidden = true;
  }
}
type.addEventListener('change', function(){hide(type.value)});      //Создаем листенер для типа эксперта, если меняется значение то передаем ее в функцию скрывания полей
