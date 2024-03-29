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
        // friend.add(this) => 이렇게 해버리면 제귀적으로 계속 동작하게 됨...
    }

    public connectCheck(friend : friend):boolean {
        const check = this.search(friend, [this]);
        if (check) return true;
        else return false;
    }

    public print(array : friend[]) {
        // ts는 배열을 그냥 console.log 할 수 없다. 때문에 직접 출력문을 만들어서 전달
        // Error : Converting circular structure to JSON 
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
            // console.log("not my friend");
            // 내가 가진 친구들로 연락해본다 애 아는애야??
            for(let a of this.friends) {
                // 연락했던 친구는 넘어감
                if (this.arraySearch(a, history)) {
                    continue;
                }
                // console.log("calling " + a.email); 
                history.push(a);
                // this.print(history);
                const check = a.search(friend, history);
                if (check === true) {
                    return check;
                }
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

function test1() {
    const a = new friend("A");
    const b = new friend("B");
    const c = new friend("C");

    a.add(b);
    b.add(c);

    console.log(a.connectCheck(c));

}

function test2() {
    const a = new friend("A");
    const b = new friend("B");
    const c = new friend("C");
    const d = new friend("D");
    const e = new friend("E");

    a.add(b);
    a.add(c);
    a.add(e);
    c.add(d);

    console.log(a.connectCheck(d));

}

function test3() {
    const a = new friend("A");
    const b = new friend("B");
    const c = new friend("C");
    const d = new friend("D");
    const e = new friend("E");
    const f = new friend("F");

    a.add(b);
    a.add(c);
    c.add(f);
    c.add(e);
    b.add(d);

    console.log(a.connectCheck(f));

}

function test4() {
    const a = new friend("A");
    const b = new friend("B");
    const c = new friend("C");
    const d = new friend("D");
    const e = new friend("E");
    const f = new friend("F");

    a.add(b);
    b.add(c);
    c.add(d);
    d.add(e);

    console.log(a.connectCheck(f));

}

function test5() {
    const a = new friend("A");
    const b = new friend("B");
    const c = new friend("C");
    const d = new friend("D");
    const e = new friend("E");
    const f = new friend("F");

    a.add(f);
    b.add(c);
    d.add(e);
    e.add(f);
    d.add(c);
    b.add(f);

    console.log(a.connectCheck(f));

}

test1()
test2()
test3()
test4()
test5()
