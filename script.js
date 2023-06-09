$('document').ready(function(){
    let arr = Array.from({length : 30}, (_, v) => v + 1)

    const shuffleArray = arr => {
        for (let i = arr.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          const temp = arr[i];
          arr[i] = arr[j];
          arr[j] = temp;
        }
    }

    shuffleArray(arr);
})
