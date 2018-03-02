window.addEventListener("load", init);

function init(){

  d3.csv("data.csv", function(data){

    // サイズ指定
    const width = 960;
    const height = 600;



    // マウス管理用のベクトル
    const mouse = new THREE.Vector2();

    const canvas = document.querySelector("#myCanvas");

    const renderer = new THREE.WebGLRenderer({
      canvas: canvas
    });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(width, height);

    





    // レンダラー作成
    /*
    const renderer = new THREE.WebGLRenderer({
      canvas: document.querySelector("#myCanvas"),
    });
    renderer.setSize(width, height);
    */

    // シーン作成
    const scene = new THREE.Scene();

    // カメラ作成
    const camera = new THREE.PerspectiveCamera(45, width/height, 1, 1000);
    camera.position.set(0, 0, 100);

    // カメラコントローラー作成
    const controls = new THREE.OrbitControls(camera);

    // 軸の表示
    var axis = new THREE.AxisHelper(100);
    scene.add(axis);
    axis.position.set(-50, -50, -50);

    var l = data.length;

    // データの長さ分の配列を作成
    //var materialList = new Array(l);
    const spriteList = [];

    for(var i = 0; i < data.length; i++){
      var n = String(i);
      var x = String(data[i].x);
      var y = String(data[i].y);
      var z = String(data[i].z);

      // 画像のテクスチャを作成
      const material = new THREE.SpriteMaterial({map: new THREE.TextureLoader().load("A_png_cut_32/" + data[i].name),});
      // スプライトを作成
      const sprite = new THREE.Sprite(material);

      // 名前情報追加
      sprite.name = data[i].name;

      // スプライトの座標を設定
      sprite.position.x = x;
      sprite.position.y = y;
      sprite.position.z = z;

      // スプライトのサイズ調整
      sprite.scale.set(2, 2, 2);

      // シーンに追加
      scene.add(sprite);

      spriteList.push(sprite);
    }

    /*
    const directionalLight = new THREE.DirectionalLight(0xFFFFFF);
    directionalLight.position.set(1, 1, 1);
    scene.add(directionalLight);

    const ambientLight = new THREE.AmbientLight(0xFFFFFF);
    scene.add(ambientLight);
    */



    // レイキャストを作成
    const raycaster = new THREE.Raycaster();


    canvas.addEventListener("mousemove", handleMouseMove);
    tick();


    function handleMouseMove(event){
      const element = event.currentTarget;
      const x = event.clientX - element.offsetLeft;
      const y = event.clientY - element.offsetTop;
      const w = element.offsetWidth;
      const h = element.offsetHeight;

      mouse.x = ( x / w ) * 2 - 1;
      mouse.y = -( y / h ) * 2 + 1;
    }

    // 毎フレーム時に実行されるループイベント
    function tick(){
      
      // マウス位置から伸びる光線ベクトルを生成
      raycaster.setFromCamera(mouse, camera);
      // その光線とぶつかったオブジェクトを得る
      const intersects = raycaster.intersectObjects(spriteList);

      spriteList.map(sprite => {
        if(intersects.length > 0 && sprite === intersects[0].object){
          console.log(sprite.name);

          $("#img").empty();
          $("#img").append("<img src='./A_png_cut/" + sprite.name + "'>")
          
          $("#name").empty();
          var name = sprite.name.slice(0, -4);
          $("#name").append("<p>" + name + "</p>");

        }
      });

      // レンダリング
      renderer.render(scene, camera);
      requestAnimationFrame(tick);


    }
  });
}



