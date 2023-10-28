const fileInput = document.getElementById('videoFile');
const uploadBtn = document.getElementById('uploadBtn');
console.log('load')
if (uploadBtn){
    uploadBtn.addEventListener('click', () => {
        const videoFile = fileInput.files[0];
        const formData = new FormData();
        formData.append('video', videoFile);
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/upload');
        xhr.onload = () => {
        console.log(xhr.responseText); 
        }
        xhr.send(formData);
  });
	
}
else{
    document.addEventListener('DOMContentLoaded', () => {  
        const fileInput = document.getElementById('videoFile');
        const uploadBtn = document.getElementById('uploadBtn');
            uploadBtn.addEventListener('click', () => {
            const videoFile = fileInput.files[0];
            const formData = new FormData();
            formData.append('video', videoFile);
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/upload');
            xhr.onload = () => {
            console.log(xhr.responseText); 
            }
            xhr.send(formData);
        });
    });

}
