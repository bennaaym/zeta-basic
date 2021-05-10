import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

const Button = ({icon,func}) => {

    return (  
        <button onClick={func} className={` text-blue-50 hover:text-blue-200 font-medium   focus:outline-none mt-1 mr-2`}>
            <FontAwesomeIcon icon={icon} size='2x'/>
        </button>
    );
}
 
export default Button;