
export default function TabButton({children, onSelect}){
    // document.querySelector("button").addEventListener("click", () =>{
    //     console.log("Button clicked!");
    // });  --> this is how it done in venilla JS when the button is clicked
    // but in React we use onClick event handler
    // above code snippet is called imperative code
    // in React we use declarative code


    return (
        <li>
            {/* Below we are passing the reference to the function instead
            of calling it because we want to react to handle the function execution 
            other wise it will be executed immediately when the component renders
             */}
            <button onClick={onSelect}>{children}</button>
        </li>
    );
}

// called components composition

// export default function TabButton({children}){
//     return (
//         <li><button>{children}</button></li>
//     );
// }