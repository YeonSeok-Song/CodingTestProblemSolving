class friend {
    public email:string;
    public friends : friend[];

    constructor(email:string) {
        this.email = email;
        this.friends = [];
    }

    public add(friend : friend) {
        this.friends.push(friend);
        friend.friends.push(this);
    }

    public connectCheck(friend : friend):boolean {
        const check = this.search(friend, [this]);
        if (check) return true;
        else return false;
    }

    public print(array : friend[]) {
        let temp = '';
        for(let x of array) {
            temp += `${x.email} `
        }
        console.log(temp);
    }

    private search(friend: friend, history: friend[]) : boolean{
        // 내가 친구이면
        if (this.arraySearch(friend, this.friends)) {
            return true;
        }
        // 내가 친구가 아니면
        else {
            console.log("not my friend");
            // 내가 가진 친구들로 연락해본다 애 아는애야??
            for(let a of this.friends) {
                // 연락했던 친구는 넘어감
                if (this.arraySearch(a, history)) {
                    continue;
                }
                console.log("calling " + a.email); 
                history.push(a);
                this.print(history);
                return a.search(friend, history);
            }
            return false;
        }
    }

    public arraySearch(node: friend, array: friend[]): boolean {

        for(let x of array) {
            if (x.email === node.email) {
                return true;
            }
        }
        return false;
    }
}

const a = new friend("A");
const b = new friend("B");
const c = new friend("C");

a.add(b);
b.add(c);

console.log(a.connectCheck(c));

