const InputField = ({
  type,
  name,
  label,
  value,
  onChange,
  className,
  placeholder,
}) => {
  return (
    <div className={`relative group ${className}`}>
      {label && (
        <label className="absolute bg-light px-[8px] text-gray text-[14px] font-[400] translate-x-[30px] -translate-y-1/2 transition-all">
          {label}
        </label>
      )}
      <input
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        className="w-full mb-10 focus:outline-none focus:border-black text-[13px] bg-transparent border border-gray rounded-[5px] py-[14.5px] px-4"
      />
    </div>
  );
};

export default InputField;
// after:ml-0.5 after:text-black after:content-['*']
