const Head = ({theme,title,textSize,fontWeight,margin}) => {
    return (
        <h1  className={`text-${textSize}  text-${theme.text} font-${fontWeight} mb-${margin}`}>{title}</h1>
    );
}
 
export default Head;