import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

const Button = ({icon,func}) => {
    return (  
        <button onClick={func} className={`bg-blue-500 hover:bg-blue-700 text-white font-medium ml-2 py-2 px-4 rounded focus:outline-none`}>
            <FontAwesomeIcon icon={icon}/>
        </button>
    );
}
 
export default Button;