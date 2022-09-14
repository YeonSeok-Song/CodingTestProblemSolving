let state: boolean = false;

function printState() {
    return new Promise((resolve, reject) => {
        if (state === false) {
            state = true;
            reject("Error");
        }
        else {
            resolve("state is true");
        }
    })
}

class limitExcute {
    attemptCount: number = 1;

    async printPormise<t> (callback: Function, tryCount: number) {
        return new Promise((resolve, reject) => {
            callback().then((value: t) => {
                resolve(value);
            }).catch((e) => {
                if (this.attemptCount >= tryCount){
                    reject("exceed count");
                } 
                else {
                    this.attemptCount++;
                    resolve(this.printPormise(callback, tryCount)); //I'm proud that I came up with this...
                }
            })
        })
    }
}

const ts = new limitExcute();
ts.printPormise(printState, 2)
    .then((value) => console.log(value))
    .catch((error) => console.log(error));
