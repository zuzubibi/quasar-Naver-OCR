import axios from 'axios'

const instance = axios.create({
    baseURL: 'http://0.0.0.0:3000/'
})

function OcrData(data){
    return instance.post('SendPhoto', data);
    
    axios.post(url, data)
    .then(function (response) {
        console.log(response);
        // console.log("정상동작");

      })
    .catch(function (error) {
        console.log(error);
        // console.log("에러났음");
    });   
}

export { OcrData };