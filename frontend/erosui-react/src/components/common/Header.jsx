import React from "react";

const Header = () => {
  return (
    <>
      <div className="flex justify-between items-center font-dmSans px-10 py-7">
        <p className="text-[14px]">Menu</p>

        <h2 className="text-3xl font-medium">EroSui</h2>

        <div className="flex gap-5 text-[14px]">
          <p>Wishlist</p>
          <p>Accout</p>
          <p className="">Cart</p>
        </div>
      </div>
      <div className="flex text-center font-dmSans text-[14px] border-y border-grayLight">
        <p className="w-full border-r border-grayLight px-5 py-1">
          All Perfumes
        </p>
        <p className="w-full border-r border-grayLight px-5 py-1">
          Men's Perfumes
        </p>
        <p className="w-full border-r border-grayLight px-5 py-1">
          Women's Perfumes
        </p>
        <p className="w-full border-r border-grayLight px-5 py-1">
          Souvenir Shop
        </p>
        <p className="w-full border-r border-grayLight px-5 py-1">Explore</p>
        <p className="w-full border-r border-grayLight px-5 py-1">Explore</p>
        <p className="w-full px-5 py-1">About</p>
      </div>
    </>
  );
};

export default Header;
