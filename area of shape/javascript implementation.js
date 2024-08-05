const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

console.log("Choose a shape to calculate the area:");
console.log("1. Circle");
console.log("2. Rectangle");
console.log("3. Triangle");

rl.question('Enter the number corresponding to the shape: ', (choice) => {
    switch (parseInt(choice)) {
        case 1:
            rl.question('Enter the radius of the circle: ', (radius) => {
                const area = Math.PI * radius * radius;
                console.log(`The area of the circle is ${area.toFixed(2)}`);
                rl.close();
            });
            break;
        case 2:
            rl.question('Enter the length of the rectangle: ', (length) => {
                rl.question('Enter the width of the rectangle: ', (width) => {
                    const area = length * width;
                    console.log(`The area of the rectangle is ${area.toFixed(2)}`);
                    rl.close();
                });
            });
            break;
        case 3:
            rl.question('Enter the base of the triangle: ', (base) => {
                rl.question('Enter the height of the triangle: ', (height) => {
                    const area = 0.5 * base * height;
                    console.log(`The area of the triangle is ${area.toFixed(2)}`);
                    rl.close();
                });
            });
            break;
        default:
            console.log('Invalid choice');
            rl.close();
    }
});
