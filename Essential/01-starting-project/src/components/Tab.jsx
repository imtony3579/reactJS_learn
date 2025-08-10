export default function Tab({children, buttons, buttonElement="menu"}){
    // Default to a 'menu' element if no buttonElement is provided
    // can also be achieved by using a different upper case props name
    // if we are using lower case then it have to be update as following variable
    const ButtonElement = buttonElement;
    return (
        <>
        <ButtonElement>
          {buttons} 
        </ButtonElement>
        {children}
        </>
    );
}